import pytest

from unittest import TestCase

from web_crawler.web_crawler import WebCrawler


@pytest.mark.e2e_tests
class TestE2E(TestCase):

    def test_2e2(self):
        # Given
        crawler = WebCrawler('http://lci.labi.fi.uba.ar/')

        # When
        web = crawler.run()

        # Then
        expected_web = 'http://lci.labi.fi.uba.ar/\n\thttp://lci.labi.fi.uba.ar/user/login?destination=node/1\n\t\thttp://lci.labi.fi.uba.ar/\n\t\thttp://lci.labi.fi.uba.ar/\n\t\thttp://lci.labi.fi.uba.ar/\n\t\thttp://lci.labi.fi.uba.ar/especificaciones\n\t\thttp://lci.labi.fi.uba.ar/precios\n\t\thttp://lci.labi.fi.uba.ar/necesario\n\t\thttp://lci.labi.fi.uba.ar/gerber\n\t\thttp://lci.labi.fi.uba.ar/scripts\n\t\thttp://labi.fi.uba.ar/sites/default/files/lci/Solicitud_PCB_materia.pdf\n\t\thttp://lci.labi.fi.uba.ar/contacto\n\t\thttp://lci.labi.fi.uba.ar/user\n\t\t\thttp://lci.labi.fi.uba.ar/\n\t\t\thttp://lci.labi.fi.uba.ar/\n\t\t\thttp://lci.labi.fi.uba.ar/\n\t\t\thttp://lci.labi.fi.uba.ar/especificaciones\n\t\t\thttp://lci.labi.fi.uba.ar/precios\n\t\t\thttp://lci.labi.fi.uba.ar/necesario\n\t\t\thttp://lci.labi.fi.uba.ar/gerber\n\t\t\thttp://lci.labi.fi.uba.ar/scripts\n\t\t\thttp://labi.fi.uba.ar/sites/default/files/lci/Solicitud_PCB_materia.pdf\n\t\t\thttp://lci.labi.fi.uba.ar/contacto\n\t\t\thttp://lci.labi.fi.uba.ar/user/password\n\t\t\thttp://drupal.org\n\t\thttp://lci.labi.fi.uba.ar/user/password\n\t\thttp://drupal.org\n\thttp://lci.labi.fi.uba.ar/especificaciones\n\thttp://lci.labi.fi.uba.ar/precios\n\thttp://lci.labi.fi.uba.ar/necesario\n\thttp://lci.labi.fi.uba.ar/gerber\n\thttp://lci.labi.fi.uba.ar/scripts\n\thttp://labi.fi.uba.ar/sites/default/files/lci/Solicitud_PCB_materia.pdf\n\thttp://lci.labi.fi.uba.ar/contacto\n\thttp://lci.labi.fi.uba.ar/especificaciones\n\thttp://labi.fi.uba.ar/sites/default/files/lci/Solicitud_PCB_materia.pdf\n\thttp://drupal.org\n'

        assert(expected_web, web)
