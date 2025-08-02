_X='hpnicfLicenseBindValidityPeriodRemaining'
_W='hpnicfLicenseOpFailedReason'
_V='hpnicfLicenseOpState'
_U='hpnicfLicenseOpString'
_T='hpnicfLicenseOpType'
_S='hpnicfLicenseOpPhysicalIndex'
_R='hpnicfLicenseIndex'
_Q='read-write'
_P='Unsigned32'
_O='OctetString'
_N='hpnicfLicenseFeatureState'
_M='hpnicfLicenseActivationFile'
_L='hpnicfLicenseOpIndex'
_K='invalid'
_J='TruthValue'
_I='hpnicfLicenseFeatureName'
_H='accessible-for-notify'
_G='read-create'
_F='hpnicfLicensePhysicalIndex'
_E='Integer32'
_D='SnmpAdminString'
_C='HPN-ICF-LICENSE-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,PhysicalIndexOrZero=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex','PhysicalIndexOrZero')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_P,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
hpnicfLicense=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,145))
if mibBuilder.loadTexts:hpnicfLicense.setRevisions(('2013-09-18 10:00',))
_HpnicfLicenseScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfLicenseScalarObjects=_HpnicfLicenseScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,145,1))
class _HpnicfLicenseNotifyEnable_Type(TruthValue):defaultValue=1
_HpnicfLicenseNotifyEnable_Type.__name__=_J
_HpnicfLicenseNotifyEnable_Object=MibScalar
hpnicfLicenseNotifyEnable=_HpnicfLicenseNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,1,1),_HpnicfLicenseNotifyEnable_Type())
hpnicfLicenseNotifyEnable.setMaxAccess(_Q)
if mibBuilder.loadTexts:hpnicfLicenseNotifyEnable.setStatus(_A)
class _HpnicfLicenseOpEntryMaxNum_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_HpnicfLicenseOpEntryMaxNum_Type.__name__=_P
_HpnicfLicenseOpEntryMaxNum_Object=MibScalar
hpnicfLicenseOpEntryMaxNum=_HpnicfLicenseOpEntryMaxNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,1,2),_HpnicfLicenseOpEntryMaxNum_Type())
hpnicfLicenseOpEntryMaxNum.setMaxAccess(_Q)
if mibBuilder.loadTexts:hpnicfLicenseOpEntryMaxNum.setStatus(_A)
_HpnicfLicenseNextFreeOpIndex_Type=Unsigned32
_HpnicfLicenseNextFreeOpIndex_Object=MibScalar
hpnicfLicenseNextFreeOpIndex=_HpnicfLicenseNextFreeOpIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,1,3),_HpnicfLicenseNextFreeOpIndex_Type())
hpnicfLicenseNextFreeOpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseNextFreeOpIndex.setStatus(_A)
_HpnicfLicenseTables_ObjectIdentity=ObjectIdentity
hpnicfLicenseTables=_HpnicfLicenseTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,145,2))
_HpnicfLicenseDevInfoTable_Object=MibTable
hpnicfLicenseDevInfoTable=_HpnicfLicenseDevInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,1))
if mibBuilder.loadTexts:hpnicfLicenseDevInfoTable.setStatus(_A)
_HpnicfLicenseDevInfoEntry_Object=MibTableRow
hpnicfLicenseDevInfoEntry=_HpnicfLicenseDevInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,1,1))
hpnicfLicenseDevInfoEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:hpnicfLicenseDevInfoEntry.setStatus(_A)
_HpnicfLicensePhysicalIndex_Type=PhysicalIndex
_HpnicfLicensePhysicalIndex_Object=MibTableColumn
hpnicfLicensePhysicalIndex=_HpnicfLicensePhysicalIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,1,1,1),_HpnicfLicensePhysicalIndex_Type())
hpnicfLicensePhysicalIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfLicensePhysicalIndex.setStatus(_A)
class _HpnicfLicenseSN_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfLicenseSN_Type.__name__=_D
_HpnicfLicenseSN_Object=MibTableColumn
hpnicfLicenseSN=_HpnicfLicenseSN_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,1,1,2),_HpnicfLicenseSN_Type())
hpnicfLicenseSN.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseSN.setStatus(_A)
class _HpnicfLicenseDeviceIDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('keyString',2),('file',3)))
_HpnicfLicenseDeviceIDType_Type.__name__=_E
_HpnicfLicenseDeviceIDType_Object=MibTableColumn
hpnicfLicenseDeviceIDType=_HpnicfLicenseDeviceIDType_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,1,1,3),_HpnicfLicenseDeviceIDType_Type())
hpnicfLicenseDeviceIDType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseDeviceIDType.setStatus(_A)
class _HpnicfLicenseDeviceID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfLicenseDeviceID_Type.__name__=_D
_HpnicfLicenseDeviceID_Object=MibTableColumn
hpnicfLicenseDeviceID=_HpnicfLicenseDeviceID_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,1,1,4),_HpnicfLicenseDeviceID_Type())
hpnicfLicenseDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseDeviceID.setStatus(_A)
class _HpnicfLicenseHardwareInfo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfLicenseHardwareInfo_Type.__name__=_D
_HpnicfLicenseHardwareInfo_Object=MibTableColumn
hpnicfLicenseHardwareInfo=_HpnicfLicenseHardwareInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,1,1,5),_HpnicfLicenseHardwareInfo_Type())
hpnicfLicenseHardwareInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseHardwareInfo.setStatus(_A)
_HpnicfLicenseMaxNum_Type=Unsigned32
_HpnicfLicenseMaxNum_Object=MibTableColumn
hpnicfLicenseMaxNum=_HpnicfLicenseMaxNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,1,1,6),_HpnicfLicenseMaxNum_Type())
hpnicfLicenseMaxNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseMaxNum.setStatus(_A)
_HpnicfLicenseUsedNum_Type=Unsigned32
_HpnicfLicenseUsedNum_Object=MibTableColumn
hpnicfLicenseUsedNum=_HpnicfLicenseUsedNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,1,1,7),_HpnicfLicenseUsedNum_Type())
hpnicfLicenseUsedNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseUsedNum.setStatus(_A)
_HpnicfLicenseRecyclableNum_Type=Unsigned32
_HpnicfLicenseRecyclableNum_Object=MibTableColumn
hpnicfLicenseRecyclableNum=_HpnicfLicenseRecyclableNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,1,1,8),_HpnicfLicenseRecyclableNum_Type())
hpnicfLicenseRecyclableNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseRecyclableNum.setStatus(_A)
class _HpnicfLicenseInstallType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('installInChassis',2),('installInSlot',3),('installInCPU',4)))
_HpnicfLicenseInstallType_Type.__name__=_E
_HpnicfLicenseInstallType_Object=MibTableColumn
hpnicfLicenseInstallType=_HpnicfLicenseInstallType_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,1,1,9),_HpnicfLicenseInstallType_Type())
hpnicfLicenseInstallType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseInstallType.setStatus(_A)
class _HpnicfLicenseFileStoragePath_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfLicenseFileStoragePath_Type.__name__=_D
_HpnicfLicenseFileStoragePath_Object=MibTableColumn
hpnicfLicenseFileStoragePath=_HpnicfLicenseFileStoragePath_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,1,1,10),_HpnicfLicenseFileStoragePath_Type())
hpnicfLicenseFileStoragePath.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseFileStoragePath.setStatus(_A)
_HpnicfLicenseGeneralTable_Object=MibTable
hpnicfLicenseGeneralTable=_HpnicfLicenseGeneralTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2))
if mibBuilder.loadTexts:hpnicfLicenseGeneralTable.setStatus(_A)
_HpnicfLicenseGeneralEntry_Object=MibTableRow
hpnicfLicenseGeneralEntry=_HpnicfLicenseGeneralEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1))
hpnicfLicenseGeneralEntry.setIndexNames((0,_C,_F),(0,_C,_R))
if mibBuilder.loadTexts:hpnicfLicenseGeneralEntry.setStatus(_A)
_HpnicfLicenseIndex_Type=Unsigned32
_HpnicfLicenseIndex_Object=MibTableColumn
hpnicfLicenseIndex=_HpnicfLicenseIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,1),_HpnicfLicenseIndex_Type())
hpnicfLicenseIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfLicenseIndex.setStatus(_A)
class _HpnicfLicenseFeature_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_HpnicfLicenseFeature_Type.__name__=_D
_HpnicfLicenseFeature_Object=MibTableColumn
hpnicfLicenseFeature=_HpnicfLicenseFeature_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,2),_HpnicfLicenseFeature_Type())
hpnicfLicenseFeature.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseFeature.setStatus(_A)
class _HpnicfLicenseProductDescr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_HpnicfLicenseProductDescr_Type.__name__=_O
_HpnicfLicenseProductDescr_Object=MibTableColumn
hpnicfLicenseProductDescr=_HpnicfLicenseProductDescr_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,3),_HpnicfLicenseProductDescr_Type())
hpnicfLicenseProductDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseProductDescr.setStatus(_A)
class _HpnicfLicenseFileDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_HpnicfLicenseFileDescr_Type.__name__=_D
_HpnicfLicenseFileDescr_Object=MibTableColumn
hpnicfLicenseFileDescr=_HpnicfLicenseFileDescr_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,4),_HpnicfLicenseFileDescr_Type())
hpnicfLicenseFileDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseFileDescr.setStatus(_A)
class _HpnicfLicenseState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),('inuse',2),('usable',3),('expired',4),('uninstalled',5),('unusable',6)))
_HpnicfLicenseState_Type.__name__=_E
_HpnicfLicenseState_Object=MibTableColumn
hpnicfLicenseState=_HpnicfLicenseState_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,5),_HpnicfLicenseState_Type())
hpnicfLicenseState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseState.setStatus(_A)
class _HpnicfLicenseActivationFile_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfLicenseActivationFile_Type.__name__=_D
_HpnicfLicenseActivationFile_Object=MibTableColumn
hpnicfLicenseActivationFile=_HpnicfLicenseActivationFile_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,6),_HpnicfLicenseActivationFile_Type())
hpnicfLicenseActivationFile.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseActivationFile.setStatus(_A)
class _HpnicfLicenseActivationKey_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfLicenseActivationKey_Type.__name__=_D
_HpnicfLicenseActivationKey_Object=MibTableColumn
hpnicfLicenseActivationKey=_HpnicfLicenseActivationKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,7),_HpnicfLicenseActivationKey_Type())
hpnicfLicenseActivationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseActivationKey.setStatus(_A)
class _HpnicfLicenseLicenseKey_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfLicenseLicenseKey_Type.__name__=_D
_HpnicfLicenseLicenseKey_Object=MibTableColumn
hpnicfLicenseLicenseKey=_HpnicfLicenseLicenseKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,8),_HpnicfLicenseLicenseKey_Type())
hpnicfLicenseLicenseKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseLicenseKey.setStatus(_A)
class _HpnicfLicenseUninstActivationFile_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfLicenseUninstActivationFile_Type.__name__=_D
_HpnicfLicenseUninstActivationFile_Object=MibTableColumn
hpnicfLicenseUninstActivationFile=_HpnicfLicenseUninstActivationFile_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,9),_HpnicfLicenseUninstActivationFile_Type())
hpnicfLicenseUninstActivationFile.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseUninstActivationFile.setStatus(_A)
class _HpnicfLicenseUninstActivationKey_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfLicenseUninstActivationKey_Type.__name__=_D
_HpnicfLicenseUninstActivationKey_Object=MibTableColumn
hpnicfLicenseUninstActivationKey=_HpnicfLicenseUninstActivationKey_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,10),_HpnicfLicenseUninstActivationKey_Type())
hpnicfLicenseUninstActivationKey.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseUninstActivationKey.setStatus(_A)
class _HpnicfLicenseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('unknown',1),('permanent',2),('daysRestricted',3),('trialDaysRestricted',4),('dateRestricted',5),('trialDateRestricted',6),('countRestricted',7),('trialCountRestricted',8)))
_HpnicfLicenseType_Type.__name__=_E
_HpnicfLicenseType_Object=MibTableColumn
hpnicfLicenseType=_HpnicfLicenseType_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,11),_HpnicfLicenseType_Type())
hpnicfLicenseType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseType.setStatus(_A)
_HpnicfLicenseInstalledTime_Type=DateAndTime
_HpnicfLicenseInstalledTime_Object=MibTableColumn
hpnicfLicenseInstalledTime=_HpnicfLicenseInstalledTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,12),_HpnicfLicenseInstalledTime_Type())
hpnicfLicenseInstalledTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseInstalledTime.setStatus(_A)
_HpnicfLicenseUninstalledTime_Type=DateAndTime
_HpnicfLicenseUninstalledTime_Object=MibTableColumn
hpnicfLicenseUninstalledTime=_HpnicfLicenseUninstalledTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,13),_HpnicfLicenseUninstalledTime_Type())
hpnicfLicenseUninstalledTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseUninstalledTime.setStatus(_A)
_HpnicfLicenseDaysLeft_Type=Unsigned32
_HpnicfLicenseDaysLeft_Object=MibTableColumn
hpnicfLicenseDaysLeft=_HpnicfLicenseDaysLeft_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,14),_HpnicfLicenseDaysLeft_Type())
hpnicfLicenseDaysLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseDaysLeft.setStatus(_A)
_HpnicfLicenseValidityStart_Type=DateAndTime
_HpnicfLicenseValidityStart_Object=MibTableColumn
hpnicfLicenseValidityStart=_HpnicfLicenseValidityStart_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,15),_HpnicfLicenseValidityStart_Type())
hpnicfLicenseValidityStart.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseValidityStart.setStatus(_A)
_HpnicfLicenseValidityEnd_Type=DateAndTime
_HpnicfLicenseValidityEnd_Object=MibTableColumn
hpnicfLicenseValidityEnd=_HpnicfLicenseValidityEnd_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,16),_HpnicfLicenseValidityEnd_Type())
hpnicfLicenseValidityEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseValidityEnd.setStatus(_A)
_HpnicfLicenseExpiredDays_Type=Unsigned32
_HpnicfLicenseExpiredDays_Object=MibTableColumn
hpnicfLicenseExpiredDays=_HpnicfLicenseExpiredDays_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,17),_HpnicfLicenseExpiredDays_Type())
hpnicfLicenseExpiredDays.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseExpiredDays.setStatus(_A)
_HpnicfLicenseCount_Type=Unsigned32
_HpnicfLicenseCount_Object=MibTableColumn
hpnicfLicenseCount=_HpnicfLicenseCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,2,1,18),_HpnicfLicenseCount_Type())
hpnicfLicenseCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseCount.setStatus(_A)
_HpnicfLicenseFeatureTable_Object=MibTable
hpnicfLicenseFeatureTable=_HpnicfLicenseFeatureTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,3))
if mibBuilder.loadTexts:hpnicfLicenseFeatureTable.setStatus(_A)
_HpnicfLicenseFeatureEntry_Object=MibTableRow
hpnicfLicenseFeatureEntry=_HpnicfLicenseFeatureEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,3,1))
hpnicfLicenseFeatureEntry.setIndexNames((0,_C,_F),(1,_C,_I))
if mibBuilder.loadTexts:hpnicfLicenseFeatureEntry.setStatus(_A)
class _HpnicfLicenseFeatureName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfLicenseFeatureName_Type.__name__=_D
_HpnicfLicenseFeatureName_Object=MibTableColumn
hpnicfLicenseFeatureName=_HpnicfLicenseFeatureName_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,3,1,1),_HpnicfLicenseFeatureName_Type())
hpnicfLicenseFeatureName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseFeatureName.setStatus(_A)
class _HpnicfLicenseFeatureState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notLicensed',1),('trialLicense',2),('formalLicense',3)))
_HpnicfLicenseFeatureState_Type.__name__=_E
_HpnicfLicenseFeatureState_Object=MibTableColumn
hpnicfLicenseFeatureState=_HpnicfLicenseFeatureState_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,3,1,2),_HpnicfLicenseFeatureState_Type())
hpnicfLicenseFeatureState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseFeatureState.setStatus(_A)
_HpnicfLicenseOpTable_Object=MibTable
hpnicfLicenseOpTable=_HpnicfLicenseOpTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,4))
if mibBuilder.loadTexts:hpnicfLicenseOpTable.setStatus(_A)
_HpnicfLicenseOpEntry_Object=MibTableRow
hpnicfLicenseOpEntry=_HpnicfLicenseOpEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,4,1))
hpnicfLicenseOpEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:hpnicfLicenseOpEntry.setStatus(_A)
_HpnicfLicenseOpIndex_Type=Unsigned32
_HpnicfLicenseOpIndex_Object=MibTableColumn
hpnicfLicenseOpIndex=_HpnicfLicenseOpIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,4,1,1),_HpnicfLicenseOpIndex_Type())
hpnicfLicenseOpIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfLicenseOpIndex.setStatus(_A)
_HpnicfLicenseOpPhysicalIndex_Type=PhysicalIndexOrZero
_HpnicfLicenseOpPhysicalIndex_Object=MibTableColumn
hpnicfLicenseOpPhysicalIndex=_HpnicfLicenseOpPhysicalIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,4,1,2),_HpnicfLicenseOpPhysicalIndex_Type())
hpnicfLicenseOpPhysicalIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLicenseOpPhysicalIndex.setStatus(_A)
class _HpnicfLicenseOpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('compress',1),('delete',2),('installActivationFile',3),('installActivationKey',4),('installLicenseKey',5),('uninstallActivationFile',6),('uninstallActivationKey',7),('uninstallLicenseKey',8)))
_HpnicfLicenseOpType_Type.__name__=_E
_HpnicfLicenseOpType_Object=MibTableColumn
hpnicfLicenseOpType=_HpnicfLicenseOpType_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,4,1,3),_HpnicfLicenseOpType_Type())
hpnicfLicenseOpType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLicenseOpType.setStatus(_A)
class _HpnicfLicenseOpString_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfLicenseOpString_Type.__name__=_D
_HpnicfLicenseOpString_Object=MibTableColumn
hpnicfLicenseOpString=_HpnicfLicenseOpString_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,4,1,4),_HpnicfLicenseOpString_Type())
hpnicfLicenseOpString.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLicenseOpString.setStatus(_A)
class _HpnicfLicenseOpNotifyEnable_Type(TruthValue):defaultValue=2
_HpnicfLicenseOpNotifyEnable_Type.__name__=_J
_HpnicfLicenseOpNotifyEnable_Object=MibTableColumn
hpnicfLicenseOpNotifyEnable=_HpnicfLicenseOpNotifyEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,4,1,5),_HpnicfLicenseOpNotifyEnable_Type())
hpnicfLicenseOpNotifyEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLicenseOpNotifyEnable.setStatus(_A)
_HpnicfLicenseOpRowStatus_Type=RowStatus
_HpnicfLicenseOpRowStatus_Object=MibTableColumn
hpnicfLicenseOpRowStatus=_HpnicfLicenseOpRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,4,1,6),_HpnicfLicenseOpRowStatus_Type())
hpnicfLicenseOpRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfLicenseOpRowStatus.setStatus(_A)
class _HpnicfLicenseOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('opInProgress',1),('opSuccessful',2),('opFailed',3)))
_HpnicfLicenseOpState_Type.__name__=_E
_HpnicfLicenseOpState_Object=MibTableColumn
hpnicfLicenseOpState=_HpnicfLicenseOpState_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,4,1,7),_HpnicfLicenseOpState_Type())
hpnicfLicenseOpState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseOpState.setStatus(_A)
class _HpnicfLicenseOpFailedReason_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfLicenseOpFailedReason_Type.__name__=_D
_HpnicfLicenseOpFailedReason_Object=MibTableColumn
hpnicfLicenseOpFailedReason=_HpnicfLicenseOpFailedReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,4,1,8),_HpnicfLicenseOpFailedReason_Type())
hpnicfLicenseOpFailedReason.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseOpFailedReason.setStatus(_A)
_HpnicfLicenseOpEndTime_Type=TimeTicks
_HpnicfLicenseOpEndTime_Object=MibTableColumn
hpnicfLicenseOpEndTime=_HpnicfLicenseOpEndTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,2,4,1,9),_HpnicfLicenseOpEndTime_Type())
hpnicfLicenseOpEndTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfLicenseOpEndTime.setStatus(_A)
_HpnicfLicenseNotifications_ObjectIdentity=ObjectIdentity
hpnicfLicenseNotifications=_HpnicfLicenseNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,145,3))
_HpnicfLicenseNotificationPrefix_ObjectIdentity=ObjectIdentity
hpnicfLicenseNotificationPrefix=_HpnicfLicenseNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,145,3,0))
_HpnicfLicenseNotificationBindings_ObjectIdentity=ObjectIdentity
hpnicfLicenseNotificationBindings=_HpnicfLicenseNotificationBindings_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,145,3,1))
_HpnicfLicenseBindValidityPeriodRemaining_Type=Unsigned32
_HpnicfLicenseBindValidityPeriodRemaining_Object=MibScalar
hpnicfLicenseBindValidityPeriodRemaining=_HpnicfLicenseBindValidityPeriodRemaining_Object((1,3,6,1,4,1,11,2,14,11,15,2,145,3,1,1),_HpnicfLicenseBindValidityPeriodRemaining_Type())
hpnicfLicenseBindValidityPeriodRemaining.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfLicenseBindValidityPeriodRemaining.setStatus(_A)
if mibBuilder.loadTexts:hpnicfLicenseBindValidityPeriodRemaining.setUnits('days')
hpnicfLicenseOpCompletion=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,145,3,0,1))
hpnicfLicenseOpCompletion.setObjects(*((_C,_L),(_C,_S),(_C,_T),(_C,_U),(_C,_V),(_C,_W)))
if mibBuilder.loadTexts:hpnicfLicenseOpCompletion.setStatus(_A)
hpnicfLicenseActivationFileLost=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,145,3,0,2))
hpnicfLicenseActivationFileLost.setObjects(*((_C,_F),(_C,_M)))
if mibBuilder.loadTexts:hpnicfLicenseActivationFileLost.setStatus(_A)
hpnicfLicenseActivationFileRestored=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,145,3,0,3))
hpnicfLicenseActivationFileRestored.setObjects(*((_C,_F),(_C,_M)))
if mibBuilder.loadTexts:hpnicfLicenseActivationFileRestored.setStatus(_A)
hpnicfLicenseExpired=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,145,3,0,4))
hpnicfLicenseExpired.setObjects(*((_C,_I),(_C,_N)))
if mibBuilder.loadTexts:hpnicfLicenseExpired.setStatus(_A)
hpnicfLicenseExpireWarning=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,145,3,0,5))
hpnicfLicenseExpireWarning.setObjects(*((_C,_I),(_C,_N),(_C,_X)))
if mibBuilder.loadTexts:hpnicfLicenseExpireWarning.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfLicense':hpnicfLicense,'hpnicfLicenseScalarObjects':hpnicfLicenseScalarObjects,'hpnicfLicenseNotifyEnable':hpnicfLicenseNotifyEnable,'hpnicfLicenseOpEntryMaxNum':hpnicfLicenseOpEntryMaxNum,'hpnicfLicenseNextFreeOpIndex':hpnicfLicenseNextFreeOpIndex,'hpnicfLicenseTables':hpnicfLicenseTables,'hpnicfLicenseDevInfoTable':hpnicfLicenseDevInfoTable,'hpnicfLicenseDevInfoEntry':hpnicfLicenseDevInfoEntry,_F:hpnicfLicensePhysicalIndex,'hpnicfLicenseSN':hpnicfLicenseSN,'hpnicfLicenseDeviceIDType':hpnicfLicenseDeviceIDType,'hpnicfLicenseDeviceID':hpnicfLicenseDeviceID,'hpnicfLicenseHardwareInfo':hpnicfLicenseHardwareInfo,'hpnicfLicenseMaxNum':hpnicfLicenseMaxNum,'hpnicfLicenseUsedNum':hpnicfLicenseUsedNum,'hpnicfLicenseRecyclableNum':hpnicfLicenseRecyclableNum,'hpnicfLicenseInstallType':hpnicfLicenseInstallType,'hpnicfLicenseFileStoragePath':hpnicfLicenseFileStoragePath,'hpnicfLicenseGeneralTable':hpnicfLicenseGeneralTable,'hpnicfLicenseGeneralEntry':hpnicfLicenseGeneralEntry,_R:hpnicfLicenseIndex,'hpnicfLicenseFeature':hpnicfLicenseFeature,'hpnicfLicenseProductDescr':hpnicfLicenseProductDescr,'hpnicfLicenseFileDescr':hpnicfLicenseFileDescr,'hpnicfLicenseState':hpnicfLicenseState,_M:hpnicfLicenseActivationFile,'hpnicfLicenseActivationKey':hpnicfLicenseActivationKey,'hpnicfLicenseLicenseKey':hpnicfLicenseLicenseKey,'hpnicfLicenseUninstActivationFile':hpnicfLicenseUninstActivationFile,'hpnicfLicenseUninstActivationKey':hpnicfLicenseUninstActivationKey,'hpnicfLicenseType':hpnicfLicenseType,'hpnicfLicenseInstalledTime':hpnicfLicenseInstalledTime,'hpnicfLicenseUninstalledTime':hpnicfLicenseUninstalledTime,'hpnicfLicenseDaysLeft':hpnicfLicenseDaysLeft,'hpnicfLicenseValidityStart':hpnicfLicenseValidityStart,'hpnicfLicenseValidityEnd':hpnicfLicenseValidityEnd,'hpnicfLicenseExpiredDays':hpnicfLicenseExpiredDays,'hpnicfLicenseCount':hpnicfLicenseCount,'hpnicfLicenseFeatureTable':hpnicfLicenseFeatureTable,'hpnicfLicenseFeatureEntry':hpnicfLicenseFeatureEntry,_I:hpnicfLicenseFeatureName,_N:hpnicfLicenseFeatureState,'hpnicfLicenseOpTable':hpnicfLicenseOpTable,'hpnicfLicenseOpEntry':hpnicfLicenseOpEntry,_L:hpnicfLicenseOpIndex,_S:hpnicfLicenseOpPhysicalIndex,_T:hpnicfLicenseOpType,_U:hpnicfLicenseOpString,'hpnicfLicenseOpNotifyEnable':hpnicfLicenseOpNotifyEnable,'hpnicfLicenseOpRowStatus':hpnicfLicenseOpRowStatus,_V:hpnicfLicenseOpState,_W:hpnicfLicenseOpFailedReason,'hpnicfLicenseOpEndTime':hpnicfLicenseOpEndTime,'hpnicfLicenseNotifications':hpnicfLicenseNotifications,'hpnicfLicenseNotificationPrefix':hpnicfLicenseNotificationPrefix,'hpnicfLicenseOpCompletion':hpnicfLicenseOpCompletion,'hpnicfLicenseActivationFileLost':hpnicfLicenseActivationFileLost,'hpnicfLicenseActivationFileRestored':hpnicfLicenseActivationFileRestored,'hpnicfLicenseExpired':hpnicfLicenseExpired,'hpnicfLicenseExpireWarning':hpnicfLicenseExpireWarning,'hpnicfLicenseNotificationBindings':hpnicfLicenseNotificationBindings,_X:hpnicfLicenseBindValidityPeriodRemaining})