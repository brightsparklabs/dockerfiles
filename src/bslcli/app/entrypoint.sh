#!/usr/bin/env bash
##
 # Installs the BSL CLI if the user has access.
 # _____________________________________________________________________________
 #
 # Created by brightSPARK Labs
 # www.brightsparklabs.com
 ##

[[ $1 == "install" ]] && cat ./template/bsl.template && exit 0

[[ -n ${BSL_CLI_EXT_SCRIPT_VERSION} ]] || {
    cat <<EOF
BSL CLI has not been installed. Please run the following:

    docker run brightsparklabs/cli install | sudo tee /usr/bin/bsl >/dev/null
    sudo chmod a+x /usr/bin/bsl
    /usr/bin/bsl

EOF
exit 0
}

export BSL_CLI_HOME="/data/cli"
export BSL_CLI_REPO="${CLI_HOME}/repo/bslcli"

[[ -d "${BSL_CLI_REPO}" ]] || {
    mkdir -p "${BSL_CLI_REPO}"
    cd "${BSL_CLI_REPO}"
    git clone git@bitbucket.org:brightsparklabs/bslcli.git .
    git checkout develop
    python -m venv "${BSL_CLI_REPO}/venv"
    . "${BSL_CLI_REPO}/venv/bin/activate"
    pip install .
}

# run bslcli
cd "${BSL_CLI_REPO}"
. venv/bin/activate
./entrypoint.py

