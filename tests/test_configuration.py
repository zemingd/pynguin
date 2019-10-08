# This file is part of Pynguin.
#
# Pynguin is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pynguin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pynguin.  If not, see <https://www.gnu.org/licenses/>.
import os

from pynguin.cli import _create_argument_parser
from pynguin.configuration import ConfigurationBuilder


def test_builder():
    builder = (
        ConfigurationBuilder()
        .set_quiet()
        .set_verbose()
        .set_log_file(os.path.join("tmp", "foo"))
    )
    configuration = builder.build()
    assert configuration.verbose
    assert configuration.quiet
    assert configuration.log_file == os.path.join("tmp", "foo")


def test_build_from_cli():
    parser = _create_argument_parser()
    args = ["--verbose", "--log-file", "/tmp/foo"]
    configuration = ConfigurationBuilder.build_from_cli_arguments(parser, args)
    assert configuration.verbose
    assert not configuration.quiet
    assert configuration.log_file == "/tmp/foo"