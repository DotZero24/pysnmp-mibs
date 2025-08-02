_M='raisecomExtendOamUpgradeDevices'
_L='raisecomExtendOamUpgradeStatusDevice'
_K='raisecomExtendOamUpgradeStatusIndex'
_J='raisecomExtendOamUpgradeIndex'
_I='TruthValue'
_H='OctetString'
_G='not-accessible'
_F='read-only'
_E='Unsigned32'
_D='RAISECOM-EXTEND-OAM-UPGRADE-MIB'
_C='Integer32'
_B='read-create'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_I)
DateAndTime,EnableVar=mibBuilder.importSymbols('SWITCH-TC','DateAndTime','EnableVar')
raisecomRemoteUpgrade=ModuleIdentity((1,3,6,1,4,1,8886,1,11))
_RaisecomExtendOamUpgradeGroup_ObjectIdentity=ObjectIdentity
raisecomExtendOamUpgradeGroup=_RaisecomExtendOamUpgradeGroup_ObjectIdentity((1,3,6,1,4,1,8886,1,11,1))
_RaisecomExtendOamUpgradeMibObjects_ObjectIdentity=ObjectIdentity
raisecomExtendOamUpgradeMibObjects=_RaisecomExtendOamUpgradeMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,11,1,1))
class _RaisecomExtendOamUpgradeNextIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RaisecomExtendOamUpgradeNextIndex_Type.__name__=_E
_RaisecomExtendOamUpgradeNextIndex_Object=MibScalar
raisecomExtendOamUpgradeNextIndex=_RaisecomExtendOamUpgradeNextIndex_Object((1,3,6,1,4,1,8886,1,11,1,1,1),_RaisecomExtendOamUpgradeNextIndex_Type())
raisecomExtendOamUpgradeNextIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomExtendOamUpgradeNextIndex.setStatus(_A)
_RaisecomExtendOamUpgradeTable_Object=MibTable
raisecomExtendOamUpgradeTable=_RaisecomExtendOamUpgradeTable_Object((1,3,6,1,4,1,8886,1,11,1,1,2))
if mibBuilder.loadTexts:raisecomExtendOamUpgradeTable.setStatus(_A)
_RaisecomExtendOamUpgradeEntry_Object=MibTableRow
raisecomExtendOamUpgradeEntry=_RaisecomExtendOamUpgradeEntry_Object((1,3,6,1,4,1,8886,1,11,1,1,2,1))
raisecomExtendOamUpgradeEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:raisecomExtendOamUpgradeEntry.setStatus(_A)
class _RaisecomExtendOamUpgradeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RaisecomExtendOamUpgradeIndex_Type.__name__=_E
_RaisecomExtendOamUpgradeIndex_Object=MibTableColumn
raisecomExtendOamUpgradeIndex=_RaisecomExtendOamUpgradeIndex_Object((1,3,6,1,4,1,8886,1,11,1,1,2,1,1),_RaisecomExtendOamUpgradeIndex_Type())
raisecomExtendOamUpgradeIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomExtendOamUpgradeIndex.setStatus(_A)
class _RaisecomExtendOamUpgradeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('download',1),('upload',2)))
_RaisecomExtendOamUpgradeType_Type.__name__=_C
_RaisecomExtendOamUpgradeType_Object=MibTableColumn
raisecomExtendOamUpgradeType=_RaisecomExtendOamUpgradeType_Object((1,3,6,1,4,1,8886,1,11,1,1,2,1,2),_RaisecomExtendOamUpgradeType_Type())
raisecomExtendOamUpgradeType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomExtendOamUpgradeType.setStatus(_A)
class _RaisecomExtendOamUpgradeFileType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('image',1),('startupconfig',2),('runningconfig',3),('others',4),('bootstrap',5),('fpga',6)))
_RaisecomExtendOamUpgradeFileType_Type.__name__=_C
_RaisecomExtendOamUpgradeFileType_Object=MibTableColumn
raisecomExtendOamUpgradeFileType=_RaisecomExtendOamUpgradeFileType_Object((1,3,6,1,4,1,8886,1,11,1,1,2,1,3),_RaisecomExtendOamUpgradeFileType_Type())
raisecomExtendOamUpgradeFileType.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomExtendOamUpgradeFileType.setStatus(_A)
_RaisecomExtendOamUpgradeFileName_Type=DisplayString
_RaisecomExtendOamUpgradeFileName_Object=MibTableColumn
raisecomExtendOamUpgradeFileName=_RaisecomExtendOamUpgradeFileName_Object((1,3,6,1,4,1,8886,1,11,1,1,2,1,4),_RaisecomExtendOamUpgradeFileName_Type())
raisecomExtendOamUpgradeFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomExtendOamUpgradeFileName.setStatus(_A)
class _RaisecomExtendOamUpgradeNotificationOnComplete_Type(TruthValue):defaultValue=2
_RaisecomExtendOamUpgradeNotificationOnComplete_Type.__name__=_I
_RaisecomExtendOamUpgradeNotificationOnComplete_Object=MibTableColumn
raisecomExtendOamUpgradeNotificationOnComplete=_RaisecomExtendOamUpgradeNotificationOnComplete_Object((1,3,6,1,4,1,8886,1,11,1,1,2,1,5),_RaisecomExtendOamUpgradeNotificationOnComplete_Type())
raisecomExtendOamUpgradeNotificationOnComplete.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomExtendOamUpgradeNotificationOnComplete.setStatus(_A)
class _RaisecomExtendOamUpgradeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('waiting',1),('getsource',2),('writedest',3),('completed',4)))
_RaisecomExtendOamUpgradeState_Type.__name__=_C
_RaisecomExtendOamUpgradeState_Object=MibTableColumn
raisecomExtendOamUpgradeState=_RaisecomExtendOamUpgradeState_Object((1,3,6,1,4,1,8886,1,11,1,1,2,1,6),_RaisecomExtendOamUpgradeState_Type())
raisecomExtendOamUpgradeState.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomExtendOamUpgradeState.setStatus(_A)
class _RaisecomExtendOamUpgradeDevices_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_RaisecomExtendOamUpgradeDevices_Type.__name__=_H
_RaisecomExtendOamUpgradeDevices_Object=MibTableColumn
raisecomExtendOamUpgradeDevices=_RaisecomExtendOamUpgradeDevices_Object((1,3,6,1,4,1,8886,1,11,1,1,2,1,7),_RaisecomExtendOamUpgradeDevices_Type())
raisecomExtendOamUpgradeDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomExtendOamUpgradeDevices.setStatus(_A)
_RaisecomExtendOamUpgradeEntryRowStatus_Type=RowStatus
_RaisecomExtendOamUpgradeEntryRowStatus_Object=MibTableColumn
raisecomExtendOamUpgradeEntryRowStatus=_RaisecomExtendOamUpgradeEntryRowStatus_Object((1,3,6,1,4,1,8886,1,11,1,1,2,1,8),_RaisecomExtendOamUpgradeEntryRowStatus_Type())
raisecomExtendOamUpgradeEntryRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raisecomExtendOamUpgradeEntryRowStatus.setStatus(_A)
_RaisecomExtendOamUpgradeStatusTable_Object=MibTable
raisecomExtendOamUpgradeStatusTable=_RaisecomExtendOamUpgradeStatusTable_Object((1,3,6,1,4,1,8886,1,11,1,1,3))
if mibBuilder.loadTexts:raisecomExtendOamUpgradeStatusTable.setStatus(_A)
_RaisecomExtendOamUpgradeStatusEntry_Object=MibTableRow
raisecomExtendOamUpgradeStatusEntry=_RaisecomExtendOamUpgradeStatusEntry_Object((1,3,6,1,4,1,8886,1,11,1,1,3,1))
raisecomExtendOamUpgradeStatusEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:raisecomExtendOamUpgradeStatusEntry.setStatus(_A)
class _RaisecomExtendOamUpgradeStatusIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RaisecomExtendOamUpgradeStatusIndex_Type.__name__=_E
_RaisecomExtendOamUpgradeStatusIndex_Object=MibTableColumn
raisecomExtendOamUpgradeStatusIndex=_RaisecomExtendOamUpgradeStatusIndex_Object((1,3,6,1,4,1,8886,1,11,1,1,3,1,1),_RaisecomExtendOamUpgradeStatusIndex_Type())
raisecomExtendOamUpgradeStatusIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomExtendOamUpgradeStatusIndex.setStatus(_A)
_RaisecomExtendOamUpgradeStatusDevice_Type=Integer32
_RaisecomExtendOamUpgradeStatusDevice_Object=MibTableColumn
raisecomExtendOamUpgradeStatusDevice=_RaisecomExtendOamUpgradeStatusDevice_Object((1,3,6,1,4,1,8886,1,11,1,1,3,1,2),_RaisecomExtendOamUpgradeStatusDevice_Type())
raisecomExtendOamUpgradeStatusDevice.setMaxAccess(_G)
if mibBuilder.loadTexts:raisecomExtendOamUpgradeStatusDevice.setStatus(_A)
class _RaisecomExtendOamUpgradeFailCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('noerror',1),('invalidfilename',2),('fileopenfail',3),('filewritefail',4),('nomem',5),('filetoolarge',6),('oamlinkbusy',7),('oamtimeout',8),('oamnotconnnected',9),('remotenotsupport',10),('unknown',11),('invalidupgradetype',12),('invalidfiletype',13),('filecheckfail',14)))
_RaisecomExtendOamUpgradeFailCause_Type.__name__=_C
_RaisecomExtendOamUpgradeFailCause_Object=MibTableColumn
raisecomExtendOamUpgradeFailCause=_RaisecomExtendOamUpgradeFailCause_Object((1,3,6,1,4,1,8886,1,11,1,1,3,1,3),_RaisecomExtendOamUpgradeFailCause_Type())
raisecomExtendOamUpgradeFailCause.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomExtendOamUpgradeFailCause.setStatus(_A)
_RaisecomExtendOamMibTraps_ObjectIdentity=ObjectIdentity
raisecomExtendOamMibTraps=_RaisecomExtendOamMibTraps_ObjectIdentity((1,3,6,1,4,1,8886,1,11,1,2))
raisecomExtendOamUpgradeCompletion=NotificationType((1,3,6,1,4,1,8886,1,11,1,2,1))
raisecomExtendOamUpgradeCompletion.setObjects((_D,_M))
if mibBuilder.loadTexts:raisecomExtendOamUpgradeCompletion.setStatus('current')
mibBuilder.exportSymbols(_D,**{'raisecomRemoteUpgrade':raisecomRemoteUpgrade,'raisecomExtendOamUpgradeGroup':raisecomExtendOamUpgradeGroup,'raisecomExtendOamUpgradeMibObjects':raisecomExtendOamUpgradeMibObjects,'raisecomExtendOamUpgradeNextIndex':raisecomExtendOamUpgradeNextIndex,'raisecomExtendOamUpgradeTable':raisecomExtendOamUpgradeTable,'raisecomExtendOamUpgradeEntry':raisecomExtendOamUpgradeEntry,_J:raisecomExtendOamUpgradeIndex,'raisecomExtendOamUpgradeType':raisecomExtendOamUpgradeType,'raisecomExtendOamUpgradeFileType':raisecomExtendOamUpgradeFileType,'raisecomExtendOamUpgradeFileName':raisecomExtendOamUpgradeFileName,'raisecomExtendOamUpgradeNotificationOnComplete':raisecomExtendOamUpgradeNotificationOnComplete,'raisecomExtendOamUpgradeState':raisecomExtendOamUpgradeState,_M:raisecomExtendOamUpgradeDevices,'raisecomExtendOamUpgradeEntryRowStatus':raisecomExtendOamUpgradeEntryRowStatus,'raisecomExtendOamUpgradeStatusTable':raisecomExtendOamUpgradeStatusTable,'raisecomExtendOamUpgradeStatusEntry':raisecomExtendOamUpgradeStatusEntry,_K:raisecomExtendOamUpgradeStatusIndex,_L:raisecomExtendOamUpgradeStatusDevice,'raisecomExtendOamUpgradeFailCause':raisecomExtendOamUpgradeFailCause,'raisecomExtendOamMibTraps':raisecomExtendOamMibTraps,'raisecomExtendOamUpgradeCompletion':raisecomExtendOamUpgradeCompletion})