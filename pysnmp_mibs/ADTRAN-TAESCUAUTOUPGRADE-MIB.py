_P='adTAeScuAutoUpgradeStatus'
_O='read-only'
_N='adTAeScuAutoUpgradeSWVerErrLevel'
_M='adGenSlotProdSwVersion'
_L='adGenSlotProdName'
_K='ADTRAN-TAESCUAUTOUPGRADE-MIB'
_J='DisplayString'
_I='Integer32'
_H='adGenSlotInfoIndex'
_G='read-write'
_F='sysName'
_E='SNMPv2-MIB'
_D='adTrapInformSeqNum'
_C='ADTRAN-GENTRAPINFORM-MIB'
_B='ADTRAN-GENSLOT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenSlotInfoIndex,adGenSlotProdName,adGenSlotProdSwVersion=mibBuilder.importSymbols(_B,_H,_L,_M)
adTrapInformSeqNum,=mibBuilder.importSymbols(_C,_D)
adTAeSCU,adTAeSCUmg,adTAeSCUmgNotificationEvents=mibBuilder.importSymbols('ADTRAN-TAeSCU-MIB','adTAeSCU','adTAeSCUmg','adTAeSCUmgNotificationEvents')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_E,_F)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
adTAeSCUAutoUpgradeMgmt=ModuleIdentity((1,3,6,1,4,1,664,2,241,11))
if mibBuilder.loadTexts:adTAeSCUAutoUpgradeMgmt.setRevisions(('2010-02-24 13:00',))
class _AdTAeScuAutoUpgradeInitiate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('initiateAutoUpgrade',1))
_AdTAeScuAutoUpgradeInitiate_Type.__name__=_I
_AdTAeScuAutoUpgradeInitiate_Object=MibScalar
adTAeScuAutoUpgradeInitiate=_AdTAeScuAutoUpgradeInitiate_Object((1,3,6,1,4,1,664,2,241,11,1),_AdTAeScuAutoUpgradeInitiate_Type())
adTAeScuAutoUpgradeInitiate.setMaxAccess(_G)
if mibBuilder.loadTexts:adTAeScuAutoUpgradeInitiate.setStatus(_A)
class _AdTAeScuAutoUpgradeCancel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('cancelAutoUpgrade',1))
_AdTAeScuAutoUpgradeCancel_Type.__name__=_I
_AdTAeScuAutoUpgradeCancel_Object=MibScalar
adTAeScuAutoUpgradeCancel=_AdTAeScuAutoUpgradeCancel_Object((1,3,6,1,4,1,664,2,241,11,2),_AdTAeScuAutoUpgradeCancel_Type())
adTAeScuAutoUpgradeCancel.setMaxAccess(_G)
if mibBuilder.loadTexts:adTAeScuAutoUpgradeCancel.setStatus(_A)
class _AdTAeScuAutoUpgradeRetries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_AdTAeScuAutoUpgradeRetries_Type.__name__=_I
_AdTAeScuAutoUpgradeRetries_Object=MibScalar
adTAeScuAutoUpgradeRetries=_AdTAeScuAutoUpgradeRetries_Object((1,3,6,1,4,1,664,2,241,11,3),_AdTAeScuAutoUpgradeRetries_Type())
adTAeScuAutoUpgradeRetries.setMaxAccess(_G)
if mibBuilder.loadTexts:adTAeScuAutoUpgradeRetries.setStatus(_A)
class _AdTAeScuAutoUpgradeRefeshInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,744))
_AdTAeScuAutoUpgradeRefeshInterval_Type.__name__=_I
_AdTAeScuAutoUpgradeRefeshInterval_Object=MibScalar
adTAeScuAutoUpgradeRefeshInterval=_AdTAeScuAutoUpgradeRefeshInterval_Object((1,3,6,1,4,1,664,2,241,11,4),_AdTAeScuAutoUpgradeRefeshInterval_Type())
adTAeScuAutoUpgradeRefeshInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:adTAeScuAutoUpgradeRefeshInterval.setStatus(_A)
class _AdTAeScuAutoUpgradeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('manual',2),('disabled',3)))
_AdTAeScuAutoUpgradeMode_Type.__name__=_I
_AdTAeScuAutoUpgradeMode_Object=MibScalar
adTAeScuAutoUpgradeMode=_AdTAeScuAutoUpgradeMode_Object((1,3,6,1,4,1,664,2,241,11,5),_AdTAeScuAutoUpgradeMode_Type())
adTAeScuAutoUpgradeMode.setMaxAccess(_G)
if mibBuilder.loadTexts:adTAeScuAutoUpgradeMode.setStatus(_A)
class _AdTAeScuAutoUpgradeConfigFilename_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AdTAeScuAutoUpgradeConfigFilename_Type.__name__=_J
_AdTAeScuAutoUpgradeConfigFilename_Object=MibScalar
adTAeScuAutoUpgradeConfigFilename=_AdTAeScuAutoUpgradeConfigFilename_Object((1,3,6,1,4,1,664,2,241,11,6),_AdTAeScuAutoUpgradeConfigFilename_Type())
adTAeScuAutoUpgradeConfigFilename.setMaxAccess(_G)
if mibBuilder.loadTexts:adTAeScuAutoUpgradeConfigFilename.setStatus(_A)
class _AdTAeScuAutoUpgradeBasePath_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_AdTAeScuAutoUpgradeBasePath_Type.__name__=_J
_AdTAeScuAutoUpgradeBasePath_Object=MibScalar
adTAeScuAutoUpgradeBasePath=_AdTAeScuAutoUpgradeBasePath_Object((1,3,6,1,4,1,664,2,241,11,7),_AdTAeScuAutoUpgradeBasePath_Type())
adTAeScuAutoUpgradeBasePath.setMaxAccess(_G)
if mibBuilder.loadTexts:adTAeScuAutoUpgradeBasePath.setStatus(_A)
class _AdTAeScuAutoUpgradeInvalidate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('discardCurrentConfigInfo',1))
_AdTAeScuAutoUpgradeInvalidate_Type.__name__=_I
_AdTAeScuAutoUpgradeInvalidate_Object=MibScalar
adTAeScuAutoUpgradeInvalidate=_AdTAeScuAutoUpgradeInvalidate_Object((1,3,6,1,4,1,664,2,241,11,8),_AdTAeScuAutoUpgradeInvalidate_Type())
adTAeScuAutoUpgradeInvalidate.setMaxAccess(_G)
if mibBuilder.loadTexts:adTAeScuAutoUpgradeInvalidate.setStatus(_A)
_AdTAeScuAutoUpgradeSystemRelease_Type=DisplayString
_AdTAeScuAutoUpgradeSystemRelease_Object=MibScalar
adTAeScuAutoUpgradeSystemRelease=_AdTAeScuAutoUpgradeSystemRelease_Object((1,3,6,1,4,1,664,2,241,11,9),_AdTAeScuAutoUpgradeSystemRelease_Type())
adTAeScuAutoUpgradeSystemRelease.setMaxAccess(_O)
if mibBuilder.loadTexts:adTAeScuAutoUpgradeSystemRelease.setStatus(_A)
_AdTAeSCUAutoUpgradeStatusTable_Object=MibTable
adTAeSCUAutoUpgradeStatusTable=_AdTAeSCUAutoUpgradeStatusTable_Object((1,3,6,1,4,1,664,2,241,11,10))
if mibBuilder.loadTexts:adTAeSCUAutoUpgradeStatusTable.setStatus(_A)
_AdTAeSCUAutoUpgradeStatusEntry_Object=MibTableRow
adTAeSCUAutoUpgradeStatusEntry=_AdTAeSCUAutoUpgradeStatusEntry_Object((1,3,6,1,4,1,664,2,241,11,10,1))
adTAeSCUAutoUpgradeStatusEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:adTAeSCUAutoUpgradeStatusEntry.setStatus(_A)
class _AdTAeScuAutoUpgradeStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AdTAeScuAutoUpgradeStatus_Type.__name__=_J
_AdTAeScuAutoUpgradeStatus_Object=MibTableColumn
adTAeScuAutoUpgradeStatus=_AdTAeScuAutoUpgradeStatus_Object((1,3,6,1,4,1,664,2,241,11,10,1,1),_AdTAeScuAutoUpgradeStatus_Type())
adTAeScuAutoUpgradeStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:adTAeScuAutoUpgradeStatus.setStatus(_A)
class _AdTAeScuAutoUpgradeSWVerErrLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5,6)));namedValues=NamedValues(*(('alert',3),('minor',4),('major',5),('critical',6)))
_AdTAeScuAutoUpgradeSWVerErrLevel_Type.__name__=_I
_AdTAeScuAutoUpgradeSWVerErrLevel_Object=MibScalar
adTAeScuAutoUpgradeSWVerErrLevel=_AdTAeScuAutoUpgradeSWVerErrLevel_Object((1,3,6,1,4,1,664,2,241,11,11),_AdTAeScuAutoUpgradeSWVerErrLevel_Type())
adTAeScuAutoUpgradeSWVerErrLevel.setMaxAccess(_G)
if mibBuilder.loadTexts:adTAeScuAutoUpgradeSWVerErrLevel.setStatus(_A)
adTAeSCUAutoUpgradeConfigChanged=NotificationType((1,3,6,1,4,1,664,1,241,0,24150))
adTAeSCUAutoUpgradeConfigChanged.setObjects(*((_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adTAeSCUAutoUpgradeConfigChanged.setStatus(_A)
adTAeSCUAutoUpgradeInvalidConfigFile=NotificationType((1,3,6,1,4,1,664,1,241,0,24152))
adTAeSCUAutoUpgradeInvalidConfigFile.setObjects(*((_C,_D),(_E,_F)))
if mibBuilder.loadTexts:adTAeSCUAutoUpgradeInvalidConfigFile.setStatus(_A)
adTAeSCUAutoUpgradeModuleUpgradeStarted=NotificationType((1,3,6,1,4,1,664,1,241,0,24154))
adTAeSCUAutoUpgradeModuleUpgradeStarted.setObjects(*((_C,_D),(_E,_F),(_B,_H)))
if mibBuilder.loadTexts:adTAeSCUAutoUpgradeModuleUpgradeStarted.setStatus(_A)
adTAeSCUAutoUpgradeModuleUpgradeCompleted=NotificationType((1,3,6,1,4,1,664,1,241,0,24156))
adTAeSCUAutoUpgradeModuleUpgradeCompleted.setObjects(*((_C,_D),(_E,_F),(_B,_H)))
if mibBuilder.loadTexts:adTAeSCUAutoUpgradeModuleUpgradeCompleted.setStatus(_A)
adTAeSCUAutoUpgradeModuleUpgradeFailed=NotificationType((1,3,6,1,4,1,664,1,241,0,24158))
adTAeSCUAutoUpgradeModuleUpgradeFailed.setObjects(*((_C,_D),(_E,_F),(_B,_H),(_K,_P)))
if mibBuilder.loadTexts:adTAeSCUAutoUpgradeModuleUpgradeFailed.setStatus(_A)
adTAeSCUAutoUpgradeUnknownModule=NotificationType((1,3,6,1,4,1,664,1,241,0,24160))
adTAeSCUAutoUpgradeUnknownModule.setObjects(*((_C,_D),(_E,_F),(_B,_H)))
if mibBuilder.loadTexts:adTAeSCUAutoUpgradeUnknownModule.setStatus(_A)
adTAAUSoftwareVerErrorClear=NotificationType((1,3,6,1,4,1,664,1,241,0,24166))
adTAAUSoftwareVerErrorClear.setObjects(*((_C,_D),(_E,_F),(_B,_H),(_B,_L),(_B,_M),(_K,_N)))
if mibBuilder.loadTexts:adTAAUSoftwareVerErrorClear.setStatus(_A)
adTAAUSoftwareVerErrorActive=NotificationType((1,3,6,1,4,1,664,1,241,0,24167))
adTAAUSoftwareVerErrorActive.setObjects(*((_C,_D),(_E,_F),(_B,_H),(_B,_L),(_B,_M),(_K,_N)))
if mibBuilder.loadTexts:adTAAUSoftwareVerErrorActive.setStatus(_A)
mibBuilder.exportSymbols(_K,**{'adTAeSCUAutoUpgradeConfigChanged':adTAeSCUAutoUpgradeConfigChanged,'adTAeSCUAutoUpgradeInvalidConfigFile':adTAeSCUAutoUpgradeInvalidConfigFile,'adTAeSCUAutoUpgradeModuleUpgradeStarted':adTAeSCUAutoUpgradeModuleUpgradeStarted,'adTAeSCUAutoUpgradeModuleUpgradeCompleted':adTAeSCUAutoUpgradeModuleUpgradeCompleted,'adTAeSCUAutoUpgradeModuleUpgradeFailed':adTAeSCUAutoUpgradeModuleUpgradeFailed,'adTAeSCUAutoUpgradeUnknownModule':adTAeSCUAutoUpgradeUnknownModule,'adTAAUSoftwareVerErrorClear':adTAAUSoftwareVerErrorClear,'adTAAUSoftwareVerErrorActive':adTAAUSoftwareVerErrorActive,'adTAeSCUAutoUpgradeMgmt':adTAeSCUAutoUpgradeMgmt,'adTAeScuAutoUpgradeInitiate':adTAeScuAutoUpgradeInitiate,'adTAeScuAutoUpgradeCancel':adTAeScuAutoUpgradeCancel,'adTAeScuAutoUpgradeRetries':adTAeScuAutoUpgradeRetries,'adTAeScuAutoUpgradeRefeshInterval':adTAeScuAutoUpgradeRefeshInterval,'adTAeScuAutoUpgradeMode':adTAeScuAutoUpgradeMode,'adTAeScuAutoUpgradeConfigFilename':adTAeScuAutoUpgradeConfigFilename,'adTAeScuAutoUpgradeBasePath':adTAeScuAutoUpgradeBasePath,'adTAeScuAutoUpgradeInvalidate':adTAeScuAutoUpgradeInvalidate,'adTAeScuAutoUpgradeSystemRelease':adTAeScuAutoUpgradeSystemRelease,'adTAeSCUAutoUpgradeStatusTable':adTAeSCUAutoUpgradeStatusTable,'adTAeSCUAutoUpgradeStatusEntry':adTAeSCUAutoUpgradeStatusEntry,_P:adTAeScuAutoUpgradeStatus,_N:adTAeScuAutoUpgradeSWVerErrLevel})