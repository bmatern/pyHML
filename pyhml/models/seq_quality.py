# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class SeqQuality(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, quality_score: int=None, sequence_end: int=None, sequence_start: int=None):
        """
        SeqQuality - a model defined in Swagger

        :param quality_score: The quality_score of this SeqQuality.
        :type quality_score: int
        :param sequence_end: The sequence_end of this SeqQuality.
        :type sequence_end: int
        :param sequence_start: The sequence_start of this SeqQuality.
        :type sequence_start: int
        """
        self.swagger_types = {
            'quality_score': int,
            'sequence_end': int,
            'sequence_start': int
        }

        self.attribute_map = {
            'quality_score': 'quality_score',
            'sequence_end': 'sequence_end',
            'sequence_start': 'sequence_start'
        }

        self._quality_score = quality_score
        self._sequence_end = sequence_end
        self._sequence_start = sequence_start

    @classmethod
    def from_dict(cls, dikt) -> 'SeqQuality':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SeqQuality of this SeqQuality.
        :rtype: SeqQuality
        """
        return deserialize_model(dikt, cls)

    @property
    def quality_score(self) -> int:
        """
        Gets the quality_score of this SeqQuality.

        :return: The quality_score of this SeqQuality.
        :rtype: int
        """
        return self._quality_score

    @quality_score.setter
    def quality_score(self, quality_score: int):
        """
        Sets the quality_score of this SeqQuality.

        :param quality_score: The quality_score of this SeqQuality.
        :type quality_score: int
        """

        self._quality_score = quality_score

    @property
    def sequence_end(self) -> int:
        """
        Gets the sequence_end of this SeqQuality.

        :return: The sequence_end of this SeqQuality.
        :rtype: int
        """
        return self._sequence_end

    @sequence_end.setter
    def sequence_end(self, sequence_end: int):
        """
        Sets the sequence_end of this SeqQuality.

        :param sequence_end: The sequence_end of this SeqQuality.
        :type sequence_end: int
        """

        self._sequence_end = sequence_end

    @property
    def sequence_start(self) -> int:
        """
        Gets the sequence_start of this SeqQuality.

        :return: The sequence_start of this SeqQuality.
        :rtype: int
        """
        return self._sequence_start

    @sequence_start.setter
    def sequence_start(self, sequence_start: int):
        """
        Sets the sequence_start of this SeqQuality.

        :param sequence_start: The sequence_start of this SeqQuality.
        :type sequence_start: int
        """

        self._sequence_start = sequence_start

