_s='celMIBGroup'
_r='celPhysicallyProgLicUseTmStamp'
_q='celPhysicallyProgLicSerialNum'
_p='celPhysicallyProgLicInstSerNum'
_o='celPhysicallyProgLicInstSysName'
_n='celPhysicallyProgLicenseStatus'
_m='celPhysicallyProgLicTypeDescr'
_l='celPhysicallyProgEntIndex'
_k='celPhysicallyProgLicenses'
_j='celOperationExpiryTmStamp'
_i='celNeededLicenses'
_h='celEntPhysicalIndex'
_g='celInUseLicenses'
_f='celInUseLicenseDescr'
_e='celPoolLicenseMaxUsage'
_d='celPoolLicensesInUse'
_c='celPoolLicensesInstalled'
_b='celPoolLicenseType'
_a='celPoolLicenseEntityVendorType'
_Z='celLicenseTypeDescr'
_Y='celLicenseConfigCount'
_X='celLicenseUpdateMethod'
_W='celLicenseUpdateSequenceNum'
_V='celLicenseConfigHistoryIndex'
_U='celLicenseUpdateTimeStamp'
_T='celLicenseInstallEntitySerNum'
_S='celLicenseSerialNumber'
_R='celLicenseEntityVendorType'
_Q='celPhysicallyProgLicenseType'
_P='celPhysicallyProgSlotNumber'
_O='celInUseLicenseType'
_N='celInUseSlotIndex'
_M='celPoolLicenseIndex'
_L='celLicenseConfigType'
_K='unknown'
_J='DisplayString'
_I='celLicenseConfigIndex'
_H='Gauge32'
_G='Integer32'
_F='Unsigned32'
_E='not-accessible'
_D='SnmpAdminString'
_C='read-only'
_B='CISCO-LICENSE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','EntPhysicalIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_H,_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
AutonomousType,DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DateAndTime',_J,'PhysAddress','TextualConvention')
ciscoLicenseMIB=ModuleIdentity((1,3,6,1,4,1,9,9,359))
if mibBuilder.loadTexts:ciscoLicenseMIB.setRevisions(('2004-01-31 00:00','2003-06-06 00:00'))
class LicenseType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_K,1),('none',2),('reserved',3),('singleService',4),('multiService',5),('channelization',6),('ima',7),('mfr',8),('rateControl',9),('multilink',10),('ppp',11)))
_CelMIBNotifications_ObjectIdentity=ObjectIdentity
celMIBNotifications=_CelMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,359,0))
_CelMIBObjects_ObjectIdentity=ObjectIdentity
celMIBObjects=_CelMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,359,1))
_CelGeneral_ObjectIdentity=ObjectIdentity
celGeneral=_CelGeneral_ObjectIdentity((1,3,6,1,4,1,9,9,359,1,1))
_CelLicenseConfigHistoryTable_Object=MibTable
celLicenseConfigHistoryTable=_CelLicenseConfigHistoryTable_Object((1,3,6,1,4,1,9,9,359,1,1,1))
if mibBuilder.loadTexts:celLicenseConfigHistoryTable.setStatus(_A)
_CelLicenseConfigHistoryEntry_Object=MibTableRow
celLicenseConfigHistoryEntry=_CelLicenseConfigHistoryEntry_Object((1,3,6,1,4,1,9,9,359,1,1,1,1))
celLicenseConfigHistoryEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:celLicenseConfigHistoryEntry.setStatus(_A)
class _CelLicenseConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CelLicenseConfigIndex_Type.__name__=_F
_CelLicenseConfigIndex_Object=MibTableColumn
celLicenseConfigIndex=_CelLicenseConfigIndex_Object((1,3,6,1,4,1,9,9,359,1,1,1,1,1),_CelLicenseConfigIndex_Type())
celLicenseConfigIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:celLicenseConfigIndex.setStatus(_A)
_CelLicenseEntityVendorType_Type=AutonomousType
_CelLicenseEntityVendorType_Object=MibTableColumn
celLicenseEntityVendorType=_CelLicenseEntityVendorType_Object((1,3,6,1,4,1,9,9,359,1,1,1,1,2),_CelLicenseEntityVendorType_Type())
celLicenseEntityVendorType.setMaxAccess(_C)
if mibBuilder.loadTexts:celLicenseEntityVendorType.setStatus(_A)
class _CelLicenseSerialNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CelLicenseSerialNumber_Type.__name__=_D
_CelLicenseSerialNumber_Object=MibTableColumn
celLicenseSerialNumber=_CelLicenseSerialNumber_Object((1,3,6,1,4,1,9,9,359,1,1,1,1,3),_CelLicenseSerialNumber_Type())
celLicenseSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:celLicenseSerialNumber.setStatus(_A)
class _CelLicenseInstallEntitySerNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CelLicenseInstallEntitySerNum_Type.__name__=_D
_CelLicenseInstallEntitySerNum_Object=MibTableColumn
celLicenseInstallEntitySerNum=_CelLicenseInstallEntitySerNum_Object((1,3,6,1,4,1,9,9,359,1,1,1,1,4),_CelLicenseInstallEntitySerNum_Type())
celLicenseInstallEntitySerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:celLicenseInstallEntitySerNum.setStatus(_A)
_CelLicenseUpdateTimeStamp_Type=DateAndTime
_CelLicenseUpdateTimeStamp_Object=MibTableColumn
celLicenseUpdateTimeStamp=_CelLicenseUpdateTimeStamp_Object((1,3,6,1,4,1,9,9,359,1,1,1,1,5),_CelLicenseUpdateTimeStamp_Type())
celLicenseUpdateTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:celLicenseUpdateTimeStamp.setStatus(_A)
_CelLicenseConfigHistoryIndex_Type=Counter32
_CelLicenseConfigHistoryIndex_Object=MibTableColumn
celLicenseConfigHistoryIndex=_CelLicenseConfigHistoryIndex_Object((1,3,6,1,4,1,9,9,359,1,1,1,1,6),_CelLicenseConfigHistoryIndex_Type())
celLicenseConfigHistoryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:celLicenseConfigHistoryIndex.setStatus(_A)
_CelLicenseUpdateSequenceNum_Type=Counter32
_CelLicenseUpdateSequenceNum_Object=MibTableColumn
celLicenseUpdateSequenceNum=_CelLicenseUpdateSequenceNum_Object((1,3,6,1,4,1,9,9,359,1,1,1,1,7),_CelLicenseUpdateSequenceNum_Type())
celLicenseUpdateSequenceNum.setMaxAccess(_C)
if mibBuilder.loadTexts:celLicenseUpdateSequenceNum.setStatus(_A)
class _CelLicenseUpdateMethod_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CelLicenseUpdateMethod_Type.__name__=_D
_CelLicenseUpdateMethod_Object=MibTableColumn
celLicenseUpdateMethod=_CelLicenseUpdateMethod_Object((1,3,6,1,4,1,9,9,359,1,1,1,1,8),_CelLicenseUpdateMethod_Type())
celLicenseUpdateMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:celLicenseUpdateMethod.setStatus(_A)
_CelLicenseConfigDetailTable_Object=MibTable
celLicenseConfigDetailTable=_CelLicenseConfigDetailTable_Object((1,3,6,1,4,1,9,9,359,1,1,2))
if mibBuilder.loadTexts:celLicenseConfigDetailTable.setStatus(_A)
_CelLicenseConfigDetailEntry_Object=MibTableRow
celLicenseConfigDetailEntry=_CelLicenseConfigDetailEntry_Object((1,3,6,1,4,1,9,9,359,1,1,2,1))
celLicenseConfigDetailEntry.setIndexNames((0,_B,_I),(0,_B,_L))
if mibBuilder.loadTexts:celLicenseConfigDetailEntry.setStatus(_A)
_CelLicenseConfigType_Type=LicenseType
_CelLicenseConfigType_Object=MibTableColumn
celLicenseConfigType=_CelLicenseConfigType_Object((1,3,6,1,4,1,9,9,359,1,1,2,1,1),_CelLicenseConfigType_Type())
celLicenseConfigType.setMaxAccess(_E)
if mibBuilder.loadTexts:celLicenseConfigType.setStatus(_A)
class _CelLicenseTypeDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CelLicenseTypeDescr_Type.__name__=_D
_CelLicenseTypeDescr_Object=MibTableColumn
celLicenseTypeDescr=_CelLicenseTypeDescr_Object((1,3,6,1,4,1,9,9,359,1,1,2,1,2),_CelLicenseTypeDescr_Type())
celLicenseTypeDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:celLicenseTypeDescr.setStatus(_A)
class _CelLicenseConfigCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CelLicenseConfigCount_Type.__name__=_F
_CelLicenseConfigCount_Object=MibTableColumn
celLicenseConfigCount=_CelLicenseConfigCount_Object((1,3,6,1,4,1,9,9,359,1,1,2,1,3),_CelLicenseConfigCount_Type())
celLicenseConfigCount.setMaxAccess(_C)
if mibBuilder.loadTexts:celLicenseConfigCount.setStatus(_A)
_CelPoolLicenseTable_Object=MibTable
celPoolLicenseTable=_CelPoolLicenseTable_Object((1,3,6,1,4,1,9,9,359,1,1,3))
if mibBuilder.loadTexts:celPoolLicenseTable.setStatus(_A)
_CelPoolLicenseEntry_Object=MibTableRow
celPoolLicenseEntry=_CelPoolLicenseEntry_Object((1,3,6,1,4,1,9,9,359,1,1,3,1))
celPoolLicenseEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:celPoolLicenseEntry.setStatus(_A)
class _CelPoolLicenseIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CelPoolLicenseIndex_Type.__name__=_F
_CelPoolLicenseIndex_Object=MibTableColumn
celPoolLicenseIndex=_CelPoolLicenseIndex_Object((1,3,6,1,4,1,9,9,359,1,1,3,1,1),_CelPoolLicenseIndex_Type())
celPoolLicenseIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:celPoolLicenseIndex.setStatus(_A)
_CelPoolLicenseEntityVendorType_Type=AutonomousType
_CelPoolLicenseEntityVendorType_Object=MibTableColumn
celPoolLicenseEntityVendorType=_CelPoolLicenseEntityVendorType_Object((1,3,6,1,4,1,9,9,359,1,1,3,1,2),_CelPoolLicenseEntityVendorType_Type())
celPoolLicenseEntityVendorType.setMaxAccess(_C)
if mibBuilder.loadTexts:celPoolLicenseEntityVendorType.setStatus(_A)
_CelPoolLicenseType_Type=LicenseType
_CelPoolLicenseType_Object=MibTableColumn
celPoolLicenseType=_CelPoolLicenseType_Object((1,3,6,1,4,1,9,9,359,1,1,3,1,3),_CelPoolLicenseType_Type())
celPoolLicenseType.setMaxAccess(_C)
if mibBuilder.loadTexts:celPoolLicenseType.setStatus(_A)
_CelPoolLicensesInstalled_Type=Gauge32
_CelPoolLicensesInstalled_Object=MibTableColumn
celPoolLicensesInstalled=_CelPoolLicensesInstalled_Object((1,3,6,1,4,1,9,9,359,1,1,3,1,4),_CelPoolLicensesInstalled_Type())
celPoolLicensesInstalled.setMaxAccess(_C)
if mibBuilder.loadTexts:celPoolLicensesInstalled.setStatus(_A)
_CelPoolLicensesInUse_Type=Gauge32
_CelPoolLicensesInUse_Object=MibTableColumn
celPoolLicensesInUse=_CelPoolLicensesInUse_Object((1,3,6,1,4,1,9,9,359,1,1,3,1,5),_CelPoolLicensesInUse_Type())
celPoolLicensesInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:celPoolLicensesInUse.setStatus(_A)
_CelPoolLicenseMaxUsage_Type=Gauge32
_CelPoolLicenseMaxUsage_Object=MibTableColumn
celPoolLicenseMaxUsage=_CelPoolLicenseMaxUsage_Object((1,3,6,1,4,1,9,9,359,1,1,3,1,6),_CelPoolLicenseMaxUsage_Type())
celPoolLicenseMaxUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:celPoolLicenseMaxUsage.setStatus(_A)
_CelInUseLicenseTable_Object=MibTable
celInUseLicenseTable=_CelInUseLicenseTable_Object((1,3,6,1,4,1,9,9,359,1,1,4))
if mibBuilder.loadTexts:celInUseLicenseTable.setStatus(_A)
_CelInUseLicenseEntry_Object=MibTableRow
celInUseLicenseEntry=_CelInUseLicenseEntry_Object((1,3,6,1,4,1,9,9,359,1,1,4,1))
celInUseLicenseEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:celInUseLicenseEntry.setStatus(_A)
class _CelInUseSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CelInUseSlotIndex_Type.__name__=_G
_CelInUseSlotIndex_Object=MibTableColumn
celInUseSlotIndex=_CelInUseSlotIndex_Object((1,3,6,1,4,1,9,9,359,1,1,4,1,1),_CelInUseSlotIndex_Type())
celInUseSlotIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:celInUseSlotIndex.setStatus(_A)
_CelInUseLicenseType_Type=LicenseType
_CelInUseLicenseType_Object=MibTableColumn
celInUseLicenseType=_CelInUseLicenseType_Object((1,3,6,1,4,1,9,9,359,1,1,4,1,2),_CelInUseLicenseType_Type())
celInUseLicenseType.setMaxAccess(_E)
if mibBuilder.loadTexts:celInUseLicenseType.setStatus(_A)
_CelEntPhysicalIndex_Type=EntPhysicalIndexOrZero
_CelEntPhysicalIndex_Object=MibTableColumn
celEntPhysicalIndex=_CelEntPhysicalIndex_Object((1,3,6,1,4,1,9,9,359,1,1,4,1,3),_CelEntPhysicalIndex_Type())
celEntPhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:celEntPhysicalIndex.setStatus(_A)
class _CelInUseLicenseDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CelInUseLicenseDescr_Type.__name__=_D
_CelInUseLicenseDescr_Object=MibTableColumn
celInUseLicenseDescr=_CelInUseLicenseDescr_Object((1,3,6,1,4,1,9,9,359,1,1,4,1,4),_CelInUseLicenseDescr_Type())
celInUseLicenseDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:celInUseLicenseDescr.setStatus(_A)
class _CelInUseLicenses_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CelInUseLicenses_Type.__name__=_H
_CelInUseLicenses_Object=MibTableColumn
celInUseLicenses=_CelInUseLicenses_Object((1,3,6,1,4,1,9,9,359,1,1,4,1,5),_CelInUseLicenses_Type())
celInUseLicenses.setMaxAccess(_C)
if mibBuilder.loadTexts:celInUseLicenses.setStatus(_A)
class _CelNeededLicenses_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CelNeededLicenses_Type.__name__=_H
_CelNeededLicenses_Object=MibTableColumn
celNeededLicenses=_CelNeededLicenses_Object((1,3,6,1,4,1,9,9,359,1,1,4,1,6),_CelNeededLicenses_Type())
celNeededLicenses.setMaxAccess(_C)
if mibBuilder.loadTexts:celNeededLicenses.setStatus(_A)
_CelOperationExpiryTmStamp_Type=DateAndTime
_CelOperationExpiryTmStamp_Object=MibTableColumn
celOperationExpiryTmStamp=_CelOperationExpiryTmStamp_Object((1,3,6,1,4,1,9,9,359,1,1,4,1,7),_CelOperationExpiryTmStamp_Type())
celOperationExpiryTmStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:celOperationExpiryTmStamp.setStatus(_A)
_CelPhysicallyProgLicenseTable_Object=MibTable
celPhysicallyProgLicenseTable=_CelPhysicallyProgLicenseTable_Object((1,3,6,1,4,1,9,9,359,1,1,5))
if mibBuilder.loadTexts:celPhysicallyProgLicenseTable.setStatus(_A)
_CelPhysicallyProgLicenseEntry_Object=MibTableRow
celPhysicallyProgLicenseEntry=_CelPhysicallyProgLicenseEntry_Object((1,3,6,1,4,1,9,9,359,1,1,5,1))
celPhysicallyProgLicenseEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:celPhysicallyProgLicenseEntry.setStatus(_A)
class _CelPhysicallyProgSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CelPhysicallyProgSlotNumber_Type.__name__=_G
_CelPhysicallyProgSlotNumber_Object=MibTableColumn
celPhysicallyProgSlotNumber=_CelPhysicallyProgSlotNumber_Object((1,3,6,1,4,1,9,9,359,1,1,5,1,1),_CelPhysicallyProgSlotNumber_Type())
celPhysicallyProgSlotNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:celPhysicallyProgSlotNumber.setStatus(_A)
_CelPhysicallyProgLicenseType_Type=LicenseType
_CelPhysicallyProgLicenseType_Object=MibTableColumn
celPhysicallyProgLicenseType=_CelPhysicallyProgLicenseType_Object((1,3,6,1,4,1,9,9,359,1,1,5,1,2),_CelPhysicallyProgLicenseType_Type())
celPhysicallyProgLicenseType.setMaxAccess(_E)
if mibBuilder.loadTexts:celPhysicallyProgLicenseType.setStatus(_A)
_CelPhysicallyProgEntIndex_Type=EntPhysicalIndexOrZero
_CelPhysicallyProgEntIndex_Object=MibTableColumn
celPhysicallyProgEntIndex=_CelPhysicallyProgEntIndex_Object((1,3,6,1,4,1,9,9,359,1,1,5,1,3),_CelPhysicallyProgEntIndex_Type())
celPhysicallyProgEntIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:celPhysicallyProgEntIndex.setStatus(_A)
class _CelPhysicallyProgLicTypeDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CelPhysicallyProgLicTypeDescr_Type.__name__=_D
_CelPhysicallyProgLicTypeDescr_Object=MibTableColumn
celPhysicallyProgLicTypeDescr=_CelPhysicallyProgLicTypeDescr_Object((1,3,6,1,4,1,9,9,359,1,1,5,1,4),_CelPhysicallyProgLicTypeDescr_Type())
celPhysicallyProgLicTypeDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:celPhysicallyProgLicTypeDescr.setStatus(_A)
class _CelPhysicallyProgLicenses_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CelPhysicallyProgLicenses_Type.__name__=_F
_CelPhysicallyProgLicenses_Object=MibTableColumn
celPhysicallyProgLicenses=_CelPhysicallyProgLicenses_Object((1,3,6,1,4,1,9,9,359,1,1,5,1,5),_CelPhysicallyProgLicenses_Type())
celPhysicallyProgLicenses.setMaxAccess(_C)
if mibBuilder.loadTexts:celPhysicallyProgLicenses.setStatus(_A)
class _CelPhysicallyProgLicenseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('noInstallableLic',2),('hasInstallableLic',3),('alreadyInstalled',4)))
_CelPhysicallyProgLicenseStatus_Type.__name__=_G
_CelPhysicallyProgLicenseStatus_Object=MibTableColumn
celPhysicallyProgLicenseStatus=_CelPhysicallyProgLicenseStatus_Object((1,3,6,1,4,1,9,9,359,1,1,5,1,6),_CelPhysicallyProgLicenseStatus_Type())
celPhysicallyProgLicenseStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:celPhysicallyProgLicenseStatus.setStatus(_A)
class _CelPhysicallyProgLicInstSysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CelPhysicallyProgLicInstSysName_Type.__name__=_J
_CelPhysicallyProgLicInstSysName_Object=MibTableColumn
celPhysicallyProgLicInstSysName=_CelPhysicallyProgLicInstSysName_Object((1,3,6,1,4,1,9,9,359,1,1,5,1,7),_CelPhysicallyProgLicInstSysName_Type())
celPhysicallyProgLicInstSysName.setMaxAccess(_C)
if mibBuilder.loadTexts:celPhysicallyProgLicInstSysName.setStatus(_A)
class _CelPhysicallyProgLicInstSerNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CelPhysicallyProgLicInstSerNum_Type.__name__=_D
_CelPhysicallyProgLicInstSerNum_Object=MibTableColumn
celPhysicallyProgLicInstSerNum=_CelPhysicallyProgLicInstSerNum_Object((1,3,6,1,4,1,9,9,359,1,1,5,1,8),_CelPhysicallyProgLicInstSerNum_Type())
celPhysicallyProgLicInstSerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:celPhysicallyProgLicInstSerNum.setStatus(_A)
class _CelPhysicallyProgLicSerialNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CelPhysicallyProgLicSerialNum_Type.__name__=_D
_CelPhysicallyProgLicSerialNum_Object=MibTableColumn
celPhysicallyProgLicSerialNum=_CelPhysicallyProgLicSerialNum_Object((1,3,6,1,4,1,9,9,359,1,1,5,1,9),_CelPhysicallyProgLicSerialNum_Type())
celPhysicallyProgLicSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:celPhysicallyProgLicSerialNum.setStatus(_A)
_CelPhysicallyProgLicUseTmStamp_Type=DateAndTime
_CelPhysicallyProgLicUseTmStamp_Object=MibTableColumn
celPhysicallyProgLicUseTmStamp=_CelPhysicallyProgLicUseTmStamp_Object((1,3,6,1,4,1,9,9,359,1,1,5,1,10),_CelPhysicallyProgLicUseTmStamp_Type())
celPhysicallyProgLicUseTmStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:celPhysicallyProgLicUseTmStamp.setStatus(_A)
_CelMIBConformance_ObjectIdentity=ObjectIdentity
celMIBConformance=_CelMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,359,2))
_CelMIBCompliances_ObjectIdentity=ObjectIdentity
celMIBCompliances=_CelMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,359,2,1))
_CelMIBGroups_ObjectIdentity=ObjectIdentity
celMIBGroups=_CelMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,359,2,2))
celMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,359,2,2,1))
celMIBGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:celMIBGroup.setStatus(_A)
celMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,359,2,1,1))
celMIBCompliance.setObjects((_B,_s))
if mibBuilder.loadTexts:celMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'LicenseType':LicenseType,'ciscoLicenseMIB':ciscoLicenseMIB,'celMIBNotifications':celMIBNotifications,'celMIBObjects':celMIBObjects,'celGeneral':celGeneral,'celLicenseConfigHistoryTable':celLicenseConfigHistoryTable,'celLicenseConfigHistoryEntry':celLicenseConfigHistoryEntry,_I:celLicenseConfigIndex,_R:celLicenseEntityVendorType,_S:celLicenseSerialNumber,_T:celLicenseInstallEntitySerNum,_U:celLicenseUpdateTimeStamp,_V:celLicenseConfigHistoryIndex,_W:celLicenseUpdateSequenceNum,_X:celLicenseUpdateMethod,'celLicenseConfigDetailTable':celLicenseConfigDetailTable,'celLicenseConfigDetailEntry':celLicenseConfigDetailEntry,_L:celLicenseConfigType,_Z:celLicenseTypeDescr,_Y:celLicenseConfigCount,'celPoolLicenseTable':celPoolLicenseTable,'celPoolLicenseEntry':celPoolLicenseEntry,_M:celPoolLicenseIndex,_a:celPoolLicenseEntityVendorType,_b:celPoolLicenseType,_c:celPoolLicensesInstalled,_d:celPoolLicensesInUse,_e:celPoolLicenseMaxUsage,'celInUseLicenseTable':celInUseLicenseTable,'celInUseLicenseEntry':celInUseLicenseEntry,_N:celInUseSlotIndex,_O:celInUseLicenseType,_h:celEntPhysicalIndex,_f:celInUseLicenseDescr,_g:celInUseLicenses,_i:celNeededLicenses,_j:celOperationExpiryTmStamp,'celPhysicallyProgLicenseTable':celPhysicallyProgLicenseTable,'celPhysicallyProgLicenseEntry':celPhysicallyProgLicenseEntry,_P:celPhysicallyProgSlotNumber,_Q:celPhysicallyProgLicenseType,_l:celPhysicallyProgEntIndex,_m:celPhysicallyProgLicTypeDescr,_k:celPhysicallyProgLicenses,_n:celPhysicallyProgLicenseStatus,_o:celPhysicallyProgLicInstSysName,_p:celPhysicallyProgLicInstSerNum,_q:celPhysicallyProgLicSerialNum,_r:celPhysicallyProgLicUseTmStamp,'celMIBConformance':celMIBConformance,'celMIBCompliances':celMIBCompliances,'celMIBCompliance':celMIBCompliance,'celMIBGroups':celMIBGroups,_s:celMIBGroup})