<?php

/**
 * PhotoTable
 * 
 * This class has been auto-generated by the Doctrine ORM Framework
 */
class PhotoTable extends PluginPhotoTable
{
    /**
     * Returns an instance of this class.
     *
     * @return PhotoTable The table instance
     */
    public static function getInstance()
    {
        return Doctrine_Core::getTable('Photo');
    }
}