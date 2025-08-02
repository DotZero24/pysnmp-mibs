_L='configFileExist'
_K='licenceIndex'
_J='instHistIndex'
_I='instIndex'
_H='DisplayStringUnsized'
_G='false'
_F='true'
_E='AT-INSTALL-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB',_H,'modules')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
install=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,49))
if mibBuilder.loadTexts:install.setRevisions(('2006-06-28 12:22',))
_InstallTrap_ObjectIdentity=ObjectIdentity
installTrap=_InstallTrap_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,49,0))
_InstallTable_Object=MibTable
installTable=_InstallTable_Object((1,3,6,1,4,1,207,8,4,4,4,49,1))
if mibBuilder.loadTexts:installTable.setStatus(_A)
_InstallEntry_Object=MibTableRow
installEntry=_InstallEntry_Object((1,3,6,1,4,1,207,8,4,4,4,49,1,1))
installEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:installEntry.setStatus(_A)
class _InstIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('temporary',1),('preferred',2),('default',3),(_A,4)))
_InstIndex_Type.__name__=_C
_InstIndex_Object=MibTableColumn
instIndex=_InstIndex_Object((1,3,6,1,4,1,207,8,4,4,4,49,1,1,1),_InstIndex_Type())
instIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:instIndex.setStatus(_A)
class _InstRelDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('eprom',2),('flash',3)))
_InstRelDevice_Type.__name__=_C
_InstRelDevice_Object=MibTableColumn
instRelDevice=_InstRelDevice_Object((1,3,6,1,4,1,207,8,4,4,4,49,1,1,2),_InstRelDevice_Type())
instRelDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:instRelDevice.setStatus(_A)
_InstRelName_Type=DisplayString
_InstRelName_Object=MibTableColumn
instRelName=_InstRelName_Object((1,3,6,1,4,1,207,8,4,4,4,49,1,1,3),_InstRelName_Type())
instRelName.setMaxAccess(_B)
if mibBuilder.loadTexts:instRelName.setStatus(_A)
_InstRelMajor_Type=Integer32
_InstRelMajor_Object=MibTableColumn
instRelMajor=_InstRelMajor_Object((1,3,6,1,4,1,207,8,4,4,4,49,1,1,4),_InstRelMajor_Type())
instRelMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:instRelMajor.setStatus(_A)
_InstRelMinor_Type=Integer32
_InstRelMinor_Object=MibTableColumn
instRelMinor=_InstRelMinor_Object((1,3,6,1,4,1,207,8,4,4,4,49,1,1,5),_InstRelMinor_Type())
instRelMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:instRelMinor.setStatus(_A)
class _InstPatDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*(('none',1),('flash',3),('nvs',4)))
_InstPatDevice_Type.__name__=_C
_InstPatDevice_Object=MibTableColumn
instPatDevice=_InstPatDevice_Object((1,3,6,1,4,1,207,8,4,4,4,49,1,1,6),_InstPatDevice_Type())
instPatDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:instPatDevice.setStatus(_A)
_InstPatName_Type=DisplayString
_InstPatName_Object=MibTableColumn
instPatName=_InstPatName_Object((1,3,6,1,4,1,207,8,4,4,4,49,1,1,7),_InstPatName_Type())
instPatName.setMaxAccess(_B)
if mibBuilder.loadTexts:instPatName.setStatus(_A)
_InstRelInterim_Type=Integer32
_InstRelInterim_Object=MibTableColumn
instRelInterim=_InstRelInterim_Object((1,3,6,1,4,1,207,8,4,4,4,49,1,1,8),_InstRelInterim_Type())
instRelInterim.setMaxAccess(_B)
if mibBuilder.loadTexts:instRelInterim.setStatus(_A)
class _InstRelExists_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_InstRelExists_Type.__name__=_C
_InstRelExists_Object=MibTableColumn
instRelExists=_InstRelExists_Object((1,3,6,1,4,1,207,8,4,4,4,49,1,1,9),_InstRelExists_Type())
instRelExists.setMaxAccess(_B)
if mibBuilder.loadTexts:instRelExists.setStatus(_A)
class _InstPatExists_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_InstPatExists_Type.__name__=_C
_InstPatExists_Object=MibTableColumn
instPatExists=_InstPatExists_Object((1,3,6,1,4,1,207,8,4,4,4,49,1,1,10),_InstPatExists_Type())
instPatExists.setMaxAccess(_B)
if mibBuilder.loadTexts:instPatExists.setStatus(_A)
_InstallHistoryTable_Object=MibTable
installHistoryTable=_InstallHistoryTable_Object((1,3,6,1,4,1,207,8,4,4,4,49,2))
if mibBuilder.loadTexts:installHistoryTable.setStatus(_A)
_InstallHistoryEntry_Object=MibTableRow
installHistoryEntry=_InstallHistoryEntry_Object((1,3,6,1,4,1,207,8,4,4,4,49,2,1))
installHistoryEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:installHistoryEntry.setStatus(_A)
_InstHistIndex_Type=Integer32
_InstHistIndex_Object=MibTableColumn
instHistIndex=_InstHistIndex_Object((1,3,6,1,4,1,207,8,4,4,4,49,2,1,1),_InstHistIndex_Type())
instHistIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:instHistIndex.setStatus(_A)
_InstHistLine_Type=DisplayString
_InstHistLine_Object=MibTableColumn
instHistLine=_InstHistLine_Object((1,3,6,1,4,1,207,8,4,4,4,49,2,1,2),_InstHistLine_Type())
instHistLine.setMaxAccess(_B)
if mibBuilder.loadTexts:instHistLine.setStatus(_A)
_ConfigFile_Type=DisplayString
_ConfigFile_Object=MibScalar
configFile=_ConfigFile_Object((1,3,6,1,4,1,207,8,4,4,4,49,3),_ConfigFile_Type())
configFile.setMaxAccess(_D)
if mibBuilder.loadTexts:configFile.setStatus(_A)
_LicenceTable_Object=MibTable
licenceTable=_LicenceTable_Object((1,3,6,1,4,1,207,8,4,4,4,49,4))
if mibBuilder.loadTexts:licenceTable.setStatus(_A)
_LicenceEntry_Object=MibTableRow
licenceEntry=_LicenceEntry_Object((1,3,6,1,4,1,207,8,4,4,4,49,4,1))
licenceEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:licenceEntry.setStatus(_A)
_LicenceIndex_Type=Integer32
_LicenceIndex_Object=MibTableColumn
licenceIndex=_LicenceIndex_Object((1,3,6,1,4,1,207,8,4,4,4,49,4,1,1),_LicenceIndex_Type())
licenceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:licenceIndex.setStatus(_A)
class _LicenceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('deleting',2)))
_LicenceStatus_Type.__name__=_C
_LicenceStatus_Object=MibTableColumn
licenceStatus=_LicenceStatus_Object((1,3,6,1,4,1,207,8,4,4,4,49,4,1,2),_LicenceStatus_Type())
licenceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:licenceStatus.setStatus(_A)
_LicenceRelease_Type=DisplayString
_LicenceRelease_Object=MibTableColumn
licenceRelease=_LicenceRelease_Object((1,3,6,1,4,1,207,8,4,4,4,49,4,1,3),_LicenceRelease_Type())
licenceRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:licenceRelease.setStatus(_A)
_LicenceMajor_Type=Integer32
_LicenceMajor_Object=MibTableColumn
licenceMajor=_LicenceMajor_Object((1,3,6,1,4,1,207,8,4,4,4,49,4,1,4),_LicenceMajor_Type())
licenceMajor.setMaxAccess(_D)
if mibBuilder.loadTexts:licenceMajor.setStatus(_A)
_LicenceMinor_Type=Integer32
_LicenceMinor_Object=MibTableColumn
licenceMinor=_LicenceMinor_Object((1,3,6,1,4,1,207,8,4,4,4,49,4,1,5),_LicenceMinor_Type())
licenceMinor.setMaxAccess(_D)
if mibBuilder.loadTexts:licenceMinor.setStatus(_A)
class _LicencePassword_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_LicencePassword_Type.__name__=_H
_LicencePassword_Object=MibTableColumn
licencePassword=_LicencePassword_Object((1,3,6,1,4,1,207,8,4,4,4,49,4,1,6),_LicencePassword_Type())
licencePassword.setMaxAccess(_D)
if mibBuilder.loadTexts:licencePassword.setStatus(_A)
_LicenceExpiry_Type=DisplayString
_LicenceExpiry_Object=MibTableColumn
licenceExpiry=_LicenceExpiry_Object((1,3,6,1,4,1,207,8,4,4,4,49,4,1,7),_LicenceExpiry_Type())
licenceExpiry.setMaxAccess(_B)
if mibBuilder.loadTexts:licenceExpiry.setStatus(_A)
_LicenceInterim_Type=Integer32
_LicenceInterim_Object=MibTableColumn
licenceInterim=_LicenceInterim_Object((1,3,6,1,4,1,207,8,4,4,4,49,4,1,8),_LicenceInterim_Type())
licenceInterim.setMaxAccess(_D)
if mibBuilder.loadTexts:licenceInterim.setStatus(_A)
_CreateConfigFile_Type=DisplayString
_CreateConfigFile_Object=MibScalar
createConfigFile=_CreateConfigFile_Object((1,3,6,1,4,1,207,8,4,4,4,49,5),_CreateConfigFile_Type())
createConfigFile.setMaxAccess(_D)
if mibBuilder.loadTexts:createConfigFile.setStatus(_A)
class _ConfigFileExist_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ConfigFileExist_Type.__name__=_C
_ConfigFileExist_Object=MibScalar
configFileExist=_ConfigFileExist_Object((1,3,6,1,4,1,207,8,4,4,4,49,6),_ConfigFileExist_Type())
configFileExist.setMaxAccess(_B)
if mibBuilder.loadTexts:configFileExist.setStatus(_A)
_CurrentConfigFile_Type=DisplayString
_CurrentConfigFile_Object=MibScalar
currentConfigFile=_CurrentConfigFile_Object((1,3,6,1,4,1,207,8,4,4,4,49,7),_CurrentConfigFile_Type())
currentConfigFile.setMaxAccess(_B)
if mibBuilder.loadTexts:currentConfigFile.setStatus(_A)
configFileExistTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,49,0,1))
configFileExistTrap.setObjects((_E,_L))
if mibBuilder.loadTexts:configFileExistTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'install':install,'installTrap':installTrap,'configFileExistTrap':configFileExistTrap,'installTable':installTable,'installEntry':installEntry,_I:instIndex,'instRelDevice':instRelDevice,'instRelName':instRelName,'instRelMajor':instRelMajor,'instRelMinor':instRelMinor,'instPatDevice':instPatDevice,'instPatName':instPatName,'instRelInterim':instRelInterim,'instRelExists':instRelExists,'instPatExists':instPatExists,'installHistoryTable':installHistoryTable,'installHistoryEntry':installHistoryEntry,_J:instHistIndex,'instHistLine':instHistLine,'configFile':configFile,'licenceTable':licenceTable,'licenceEntry':licenceEntry,_K:licenceIndex,'licenceStatus':licenceStatus,'licenceRelease':licenceRelease,'licenceMajor':licenceMajor,'licenceMinor':licenceMinor,'licencePassword':licencePassword,'licenceExpiry':licenceExpiry,'licenceInterim':licenceInterim,'createConfigFile':createConfigFile,_L:configFileExist,'currentConfigFile':currentConfigFile})