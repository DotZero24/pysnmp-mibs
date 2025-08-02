_B4='ciscoScsiDeviceGroup'
_B3='ciscoScsiLuStatusChanged'
_B2='ciscoScsiTgtDevStatusChanged'
_B1='ciscoScsiPortBusyStatuses'
_B0='ciscoScsiDeviceResets'
_A_='ciscoScsiDscTgtHSInCommands'
_Az='ciscoScsiDscTgtWrMegaBytes'
_Ay='ciscoScsiDscTgtReadMegaBytes'
_Ax='ciscoScsiDscTgtInCommands'
_Aw='ciscoScsiIntrPrtHSOutCommands'
_Av='ciscoScsiIntrPrtReadMegaBytes'
_Au='ciscoScsiIntrPrtWrMegaBytes'
_At='ciscoScsiIntrPrtOutCommands'
_As='ciscoScsiIntrDevOutResets'
_Ar='ciscoScsiAuthIntrHSOutCommands'
_Aq='ciscoScsiAuthIntrWrMegaBytes'
_Ap='ciscoScsiAuthIntrReadMegaBytes'
_Ao='ciscoScsiAuthIntrOutCommands'
_An='ciscoScsiAuthIntrAttachedTimes'
_Am='ciscoScsiLuHSInCommands'
_Al='ciscoScsiTgtPortHSInCommands'
_Ak='ciscoScsiLuOutQueueFullStatus'
_Aj='ciscoScsiLuInResets'
_Ai='ciscoScsiLuWrittenMegaBytes'
_Ah='ciscoScsiLuReadMegaBytes'
_Ag='ciscoScsiLuInCommands'
_Af='ciscoScsiTgtPortReadMegaBytes'
_Ae='ciscoScsiTgtPortWrMegaBytes'
_Ad='ciscoScsiTgtPortInCommands'
_Ac='ciscoScsiAuthIntrRowStatus'
_Ab='ciscoScsiAuthIntrLastCreation'
_Aa='ciscoScsiAuthIntrLunMapIndex'
_AZ='ciscoScsiAuthIntrName'
_AY='ciscoScsiAuthIntrDevOrPort'
_AX='ciscoScsiLunMapRowStatus'
_AW='ciscoScsiLunMapLuIndex'
_AV='ciscoScsiLuIdValue'
_AU='ciscoScsiLuIdType'
_AT='ciscoScsiLuIdAssociation'
_AS='ciscoScsiLuIdCodeSet'
_AR='ciscoScsiLuState'
_AQ='ciscoScsiLuPeripheralType'
_AP='ciscoScsiLuRevisionId'
_AO='ciscoScsiLuProductId'
_AN='ciscoScsiLuVendorId'
_AM='ciscoScsiLuWwnName'
_AL='ciscoScsiLuDefaultLun'
_AK='ciscoScsiAttIntrPrtId'
_AJ='ciscoScsiAttIntrPrtName'
_AI='ciscoScsiAttIntrPrtAuthIntrIdx'
_AH='ciscoScsiTgtPortIdentifier'
_AG='ciscoScsiTgtPortName'
_AF='ciscoScsiTgtDevNonAccLUs'
_AE='ciscoScsiTgtDevNumberOfLUs'
_AD='ciscoScsiDscLunIdValue'
_AC='ciscoScsiDscLunIdType'
_AB='ciscoScsiDscLunIdAssociation'
_AA='ciscoScsiDscLunIdCodeSet'
_A9='ciscoScsiDscLunLun'
_A8='ciscoScsiDscTgtLastCreation'
_A7='ciscoScsiDscTgtRowStatus'
_A6='ciscoScsiDscTgtDiscovered'
_A5='ciscoScsiDscTgtConfigured'
_A4='ciscoScsiDscTgtName'
_A3='ciscoScsiDscTgtDevOrPort'
_A2='ciscoScsiAttTgtPortIdentifier'
_A1='ciscoScsiAttTgtPortName'
_A0='ciscoScsiAttTgtPortDscTgtIdx'
_z='ciscoScsiIntrPrtIdentifier'
_y='ciscoScsiIntrPrtName'
_x='ciscoScsiIntrDevAccMode'
_w='ciscoScsiTrnsptDevName'
_v='ciscoScsiTrnsptPointer'
_u='ciscoScsiTrnsptType'
_t='ciscoScsiPortTrnsptPtr'
_s='ciscoScsiPortRole'
_r='ciscoScsiDevicePortNumber'
_q='ciscoScsiDeviceRole'
_p='ciscoScsiDeviceAlias'
_o='ciscoScsiInstNotifEnable'
_n='ciscoScsiInstVendorVersion'
_m='ciscoScsiInstSoftwareIndex'
_l='ciscoScsiInstAlias'
_k='ciscoScsiLunMapLun'
_j='ciscoScsiLunMapIndex'
_i='ciscoScsiLuIdIndex'
_h='ciscoScsiAttIntrPrtIdx'
_g='ciscoScsiAuthIntrIndex'
_f='ciscoScsiAuthIntrTgtPortIndex'
_e='abnormal'
_d='readying'
_c='broken'
_b='available'
_a='ciscoScsiAttTgtPortIndex'
_Z='ciscoScsiDscLunIdIndex'
_Y='ciscoScsiTrnsptIndex'
_X='initiator'
_W='target'
_V='ciscoScsiLuStatus'
_U='ciscoScsiTgtDeviceStatus'
_T='ciscoScsiLuIndex'
_S='ciscoScsiDscLunIndex'
_R='unknown'
_Q='TruthValue'
_P='ciscoScsiDscTgtIndex'
_O='ciscoScsiDscTgtIntrPortIndex'
_N='read-write'
_M='Integer32'
_L='Bits'
_K='ciscoScsiPortIndex'
_J='SnmpAdminString'
_I='read-create'
_H='Megabytes'
_G='commands'
_F='not-accessible'
_E='ciscoScsiDeviceIndex'
_D='ciscoScsiInstIndex'
_C='read-only'
_B='CISCO-SCSI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_L,'Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp',_Q)
ciscoScsiMIB=ModuleIdentity((1,3,6,1,4,1,9,10,95))
if mibBuilder.loadTexts:ciscoScsiMIB.setRevisions(('2002-12-31 00:00','2002-11-08 00:00','2002-10-05 00:00'))
class ScsiLUNOrZero(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(2,2),ValueSizeConstraint(8,8))
class ScsiIndexValue(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class ScsiPortIndexValueOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class ScsiIndexValueOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class ScsiIdentifier(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,1),ValueSizeConstraint(2,2),ValueSizeConstraint(3,3),ValueSizeConstraint(11,11),ValueSizeConstraint(16,16),ValueSizeConstraint(256,256),ValueSizeConstraint(258,258),ValueSizeConstraint(262,262))
class ScsiName(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8),ValueSizeConstraint(11,11),ValueSizeConstraint(16,16),ValueSizeConstraint(256,256),ValueSizeConstraint(258,258),ValueSizeConstraint(262,262))
class ScsiNameIdOrZero(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8))
class ScsiDeviceOrPort(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('device',1),('port',2),('other',3)))
class ScsiIdCodeSet(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
class ScsiIdAssociation(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
class ScsiIdType(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
class ScsiIdValue(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
class HrSWInstalledIndexOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CiscoScsiObjects_ObjectIdentity=ObjectIdentity
ciscoScsiObjects=_CiscoScsiObjects_ObjectIdentity((1,3,6,1,4,1,9,10,95,1))
_CiscoScsiTransportTypes_ObjectIdentity=ObjectIdentity
ciscoScsiTransportTypes=_CiscoScsiTransportTypes_ObjectIdentity((1,3,6,1,4,1,9,10,95,1,1))
_CiscoScsiTranportOther_ObjectIdentity=ObjectIdentity
ciscoScsiTranportOther=_CiscoScsiTranportOther_ObjectIdentity((1,3,6,1,4,1,9,10,95,1,1,1))
_CiscoScsiTranportSPI_ObjectIdentity=ObjectIdentity
ciscoScsiTranportSPI=_CiscoScsiTranportSPI_ObjectIdentity((1,3,6,1,4,1,9,10,95,1,1,2))
_CiscoScsiTransportFCP_ObjectIdentity=ObjectIdentity
ciscoScsiTransportFCP=_CiscoScsiTransportFCP_ObjectIdentity((1,3,6,1,4,1,9,10,95,1,1,3))
_CiscoScsiTransportSRP_ObjectIdentity=ObjectIdentity
ciscoScsiTransportSRP=_CiscoScsiTransportSRP_ObjectIdentity((1,3,6,1,4,1,9,10,95,1,1,4))
_CiscoScsiTransportISCSI_ObjectIdentity=ObjectIdentity
ciscoScsiTransportISCSI=_CiscoScsiTransportISCSI_ObjectIdentity((1,3,6,1,4,1,9,10,95,1,1,5))
_CiscoScsiTransportSBP_ObjectIdentity=ObjectIdentity
ciscoScsiTransportSBP=_CiscoScsiTransportSBP_ObjectIdentity((1,3,6,1,4,1,9,10,95,1,1,6))
_CiscoScsiGeneral_ObjectIdentity=ObjectIdentity
ciscoScsiGeneral=_CiscoScsiGeneral_ObjectIdentity((1,3,6,1,4,1,9,10,95,1,2))
_CiscoScsiInstanceTable_Object=MibTable
ciscoScsiInstanceTable=_CiscoScsiInstanceTable_Object((1,3,6,1,4,1,9,10,95,1,2,1))
if mibBuilder.loadTexts:ciscoScsiInstanceTable.setStatus(_A)
_CiscoScsiInstanceEntry_Object=MibTableRow
ciscoScsiInstanceEntry=_CiscoScsiInstanceEntry_Object((1,3,6,1,4,1,9,10,95,1,2,1,1))
ciscoScsiInstanceEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:ciscoScsiInstanceEntry.setStatus(_A)
_CiscoScsiInstIndex_Type=ScsiIndexValue
_CiscoScsiInstIndex_Object=MibTableColumn
ciscoScsiInstIndex=_CiscoScsiInstIndex_Object((1,3,6,1,4,1,9,10,95,1,2,1,1,1),_CiscoScsiInstIndex_Type())
ciscoScsiInstIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiInstIndex.setStatus(_A)
class _CiscoScsiInstAlias_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_CiscoScsiInstAlias_Type.__name__=_J
_CiscoScsiInstAlias_Object=MibTableColumn
ciscoScsiInstAlias=_CiscoScsiInstAlias_Object((1,3,6,1,4,1,9,10,95,1,2,1,1,2),_CiscoScsiInstAlias_Type())
ciscoScsiInstAlias.setMaxAccess(_N)
if mibBuilder.loadTexts:ciscoScsiInstAlias.setStatus(_A)
_CiscoScsiInstSoftwareIndex_Type=HrSWInstalledIndexOrZero
_CiscoScsiInstSoftwareIndex_Object=MibTableColumn
ciscoScsiInstSoftwareIndex=_CiscoScsiInstSoftwareIndex_Object((1,3,6,1,4,1,9,10,95,1,2,1,1,3),_CiscoScsiInstSoftwareIndex_Type())
ciscoScsiInstSoftwareIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiInstSoftwareIndex.setStatus(_A)
class _CiscoScsiInstVendorVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_CiscoScsiInstVendorVersion_Type.__name__=_J
_CiscoScsiInstVendorVersion_Object=MibTableColumn
ciscoScsiInstVendorVersion=_CiscoScsiInstVendorVersion_Object((1,3,6,1,4,1,9,10,95,1,2,1,1,4),_CiscoScsiInstVendorVersion_Type())
ciscoScsiInstVendorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiInstVendorVersion.setStatus(_A)
class _CiscoScsiInstNotifEnable_Type(TruthValue):defaultValue=1
_CiscoScsiInstNotifEnable_Type.__name__=_Q
_CiscoScsiInstNotifEnable_Object=MibTableColumn
ciscoScsiInstNotifEnable=_CiscoScsiInstNotifEnable_Object((1,3,6,1,4,1,9,10,95,1,2,1,1,5),_CiscoScsiInstNotifEnable_Type())
ciscoScsiInstNotifEnable.setMaxAccess(_N)
if mibBuilder.loadTexts:ciscoScsiInstNotifEnable.setStatus(_A)
_CiscoScsiDeviceTable_Object=MibTable
ciscoScsiDeviceTable=_CiscoScsiDeviceTable_Object((1,3,6,1,4,1,9,10,95,1,2,2))
if mibBuilder.loadTexts:ciscoScsiDeviceTable.setStatus(_A)
_CiscoScsiDeviceEntry_Object=MibTableRow
ciscoScsiDeviceEntry=_CiscoScsiDeviceEntry_Object((1,3,6,1,4,1,9,10,95,1,2,2,1))
ciscoScsiDeviceEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:ciscoScsiDeviceEntry.setStatus(_A)
_CiscoScsiDeviceIndex_Type=ScsiIndexValue
_CiscoScsiDeviceIndex_Object=MibTableColumn
ciscoScsiDeviceIndex=_CiscoScsiDeviceIndex_Object((1,3,6,1,4,1,9,10,95,1,2,2,1,1),_CiscoScsiDeviceIndex_Type())
ciscoScsiDeviceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiDeviceIndex.setStatus(_A)
class _CiscoScsiDeviceAlias_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_CiscoScsiDeviceAlias_Type.__name__=_J
_CiscoScsiDeviceAlias_Object=MibTableColumn
ciscoScsiDeviceAlias=_CiscoScsiDeviceAlias_Object((1,3,6,1,4,1,9,10,95,1,2,2,1,2),_CiscoScsiDeviceAlias_Type())
ciscoScsiDeviceAlias.setMaxAccess(_N)
if mibBuilder.loadTexts:ciscoScsiDeviceAlias.setStatus(_A)
class _CiscoScsiDeviceRole_Type(Bits):namedValues=NamedValues(*((_W,0),(_X,1)))
_CiscoScsiDeviceRole_Type.__name__=_L
_CiscoScsiDeviceRole_Object=MibTableColumn
ciscoScsiDeviceRole=_CiscoScsiDeviceRole_Object((1,3,6,1,4,1,9,10,95,1,2,2,1,3),_CiscoScsiDeviceRole_Type())
ciscoScsiDeviceRole.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDeviceRole.setStatus(_A)
_CiscoScsiDevicePortNumber_Type=Unsigned32
_CiscoScsiDevicePortNumber_Object=MibTableColumn
ciscoScsiDevicePortNumber=_CiscoScsiDevicePortNumber_Object((1,3,6,1,4,1,9,10,95,1,2,2,1,4),_CiscoScsiDevicePortNumber_Type())
ciscoScsiDevicePortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDevicePortNumber.setStatus(_A)
_CiscoScsiDeviceResets_Type=Counter32
_CiscoScsiDeviceResets_Object=MibTableColumn
ciscoScsiDeviceResets=_CiscoScsiDeviceResets_Object((1,3,6,1,4,1,9,10,95,1,2,2,1,5),_CiscoScsiDeviceResets_Type())
ciscoScsiDeviceResets.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDeviceResets.setStatus(_A)
_CiscoScsiPortTable_Object=MibTable
ciscoScsiPortTable=_CiscoScsiPortTable_Object((1,3,6,1,4,1,9,10,95,1,2,3))
if mibBuilder.loadTexts:ciscoScsiPortTable.setStatus(_A)
_CiscoScsiPortEntry_Object=MibTableRow
ciscoScsiPortEntry=_CiscoScsiPortEntry_Object((1,3,6,1,4,1,9,10,95,1,2,3,1))
ciscoScsiPortEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_K))
if mibBuilder.loadTexts:ciscoScsiPortEntry.setStatus(_A)
_CiscoScsiPortIndex_Type=ScsiIndexValue
_CiscoScsiPortIndex_Object=MibTableColumn
ciscoScsiPortIndex=_CiscoScsiPortIndex_Object((1,3,6,1,4,1,9,10,95,1,2,3,1,1),_CiscoScsiPortIndex_Type())
ciscoScsiPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiPortIndex.setStatus(_A)
class _CiscoScsiPortRole_Type(Bits):namedValues=NamedValues(*((_W,0),(_X,1)))
_CiscoScsiPortRole_Type.__name__=_L
_CiscoScsiPortRole_Object=MibTableColumn
ciscoScsiPortRole=_CiscoScsiPortRole_Object((1,3,6,1,4,1,9,10,95,1,2,3,1,2),_CiscoScsiPortRole_Type())
ciscoScsiPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiPortRole.setStatus(_A)
_CiscoScsiPortTrnsptPtr_Type=RowPointer
_CiscoScsiPortTrnsptPtr_Object=MibTableColumn
ciscoScsiPortTrnsptPtr=_CiscoScsiPortTrnsptPtr_Object((1,3,6,1,4,1,9,10,95,1,2,3,1,3),_CiscoScsiPortTrnsptPtr_Type())
ciscoScsiPortTrnsptPtr.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiPortTrnsptPtr.setStatus(_A)
_CiscoScsiPortBusyStatuses_Type=Counter32
_CiscoScsiPortBusyStatuses_Object=MibTableColumn
ciscoScsiPortBusyStatuses=_CiscoScsiPortBusyStatuses_Object((1,3,6,1,4,1,9,10,95,1,2,3,1,4),_CiscoScsiPortBusyStatuses_Type())
ciscoScsiPortBusyStatuses.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiPortBusyStatuses.setStatus(_A)
_CiscoScsiTrnsptTable_Object=MibTable
ciscoScsiTrnsptTable=_CiscoScsiTrnsptTable_Object((1,3,6,1,4,1,9,10,95,1,2,5))
if mibBuilder.loadTexts:ciscoScsiTrnsptTable.setStatus(_A)
_CiscoScsiTrnsptEntry_Object=MibTableRow
ciscoScsiTrnsptEntry=_CiscoScsiTrnsptEntry_Object((1,3,6,1,4,1,9,10,95,1,2,5,1))
ciscoScsiTrnsptEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_Y))
if mibBuilder.loadTexts:ciscoScsiTrnsptEntry.setStatus(_A)
_CiscoScsiTrnsptIndex_Type=ScsiIndexValue
_CiscoScsiTrnsptIndex_Object=MibTableColumn
ciscoScsiTrnsptIndex=_CiscoScsiTrnsptIndex_Object((1,3,6,1,4,1,9,10,95,1,2,5,1,1),_CiscoScsiTrnsptIndex_Type())
ciscoScsiTrnsptIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiTrnsptIndex.setStatus(_A)
_CiscoScsiTrnsptType_Type=AutonomousType
_CiscoScsiTrnsptType_Object=MibTableColumn
ciscoScsiTrnsptType=_CiscoScsiTrnsptType_Object((1,3,6,1,4,1,9,10,95,1,2,5,1,2),_CiscoScsiTrnsptType_Type())
ciscoScsiTrnsptType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiTrnsptType.setStatus(_A)
_CiscoScsiTrnsptPointer_Type=RowPointer
_CiscoScsiTrnsptPointer_Object=MibTableColumn
ciscoScsiTrnsptPointer=_CiscoScsiTrnsptPointer_Object((1,3,6,1,4,1,9,10,95,1,2,5,1,3),_CiscoScsiTrnsptPointer_Type())
ciscoScsiTrnsptPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiTrnsptPointer.setStatus(_A)
_CiscoScsiTrnsptDevName_Type=ScsiName
_CiscoScsiTrnsptDevName_Object=MibTableColumn
ciscoScsiTrnsptDevName=_CiscoScsiTrnsptDevName_Object((1,3,6,1,4,1,9,10,95,1,2,5,1,4),_CiscoScsiTrnsptDevName_Type())
ciscoScsiTrnsptDevName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiTrnsptDevName.setStatus(_A)
_CiscoScsiInitiator_ObjectIdentity=ObjectIdentity
ciscoScsiInitiator=_CiscoScsiInitiator_ObjectIdentity((1,3,6,1,4,1,9,10,95,1,3))
_CiscoScsiIntrDevTable_Object=MibTable
ciscoScsiIntrDevTable=_CiscoScsiIntrDevTable_Object((1,3,6,1,4,1,9,10,95,1,3,1))
if mibBuilder.loadTexts:ciscoScsiIntrDevTable.setStatus(_A)
_CiscoScsiIntrDevEntry_Object=MibTableRow
ciscoScsiIntrDevEntry=_CiscoScsiIntrDevEntry_Object((1,3,6,1,4,1,9,10,95,1,3,1,1))
ciscoScsiIntrDevEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:ciscoScsiIntrDevEntry.setStatus(_A)
class _CiscoScsiIntrDevAccMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('autoEnable',2),('manualEnable',3)))
_CiscoScsiIntrDevAccMode_Type.__name__=_M
_CiscoScsiIntrDevAccMode_Object=MibTableColumn
ciscoScsiIntrDevAccMode=_CiscoScsiIntrDevAccMode_Object((1,3,6,1,4,1,9,10,95,1,3,1,1,1),_CiscoScsiIntrDevAccMode_Type())
ciscoScsiIntrDevAccMode.setMaxAccess(_N)
if mibBuilder.loadTexts:ciscoScsiIntrDevAccMode.setStatus(_A)
_CiscoScsiIntrDevOutResets_Type=Counter32
_CiscoScsiIntrDevOutResets_Object=MibTableColumn
ciscoScsiIntrDevOutResets=_CiscoScsiIntrDevOutResets_Object((1,3,6,1,4,1,9,10,95,1,3,1,1,2),_CiscoScsiIntrDevOutResets_Type())
ciscoScsiIntrDevOutResets.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiIntrDevOutResets.setStatus(_A)
_CiscoScsiIntrPrtTable_Object=MibTable
ciscoScsiIntrPrtTable=_CiscoScsiIntrPrtTable_Object((1,3,6,1,4,1,9,10,95,1,3,3))
if mibBuilder.loadTexts:ciscoScsiIntrPrtTable.setStatus(_A)
_CiscoScsiIntrPrtEntry_Object=MibTableRow
ciscoScsiIntrPrtEntry=_CiscoScsiIntrPrtEntry_Object((1,3,6,1,4,1,9,10,95,1,3,3,1))
ciscoScsiIntrPrtEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_K))
if mibBuilder.loadTexts:ciscoScsiIntrPrtEntry.setStatus(_A)
_CiscoScsiIntrPrtName_Type=ScsiName
_CiscoScsiIntrPrtName_Object=MibTableColumn
ciscoScsiIntrPrtName=_CiscoScsiIntrPrtName_Object((1,3,6,1,4,1,9,10,95,1,3,3,1,1),_CiscoScsiIntrPrtName_Type())
ciscoScsiIntrPrtName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiIntrPrtName.setStatus(_A)
_CiscoScsiIntrPrtIdentifier_Type=ScsiIdentifier
_CiscoScsiIntrPrtIdentifier_Object=MibTableColumn
ciscoScsiIntrPrtIdentifier=_CiscoScsiIntrPrtIdentifier_Object((1,3,6,1,4,1,9,10,95,1,3,3,1,2),_CiscoScsiIntrPrtIdentifier_Type())
ciscoScsiIntrPrtIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiIntrPrtIdentifier.setStatus(_A)
_CiscoScsiIntrPrtOutCommands_Type=Counter32
_CiscoScsiIntrPrtOutCommands_Object=MibTableColumn
ciscoScsiIntrPrtOutCommands=_CiscoScsiIntrPrtOutCommands_Object((1,3,6,1,4,1,9,10,95,1,3,3,1,3),_CiscoScsiIntrPrtOutCommands_Type())
ciscoScsiIntrPrtOutCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiIntrPrtOutCommands.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiIntrPrtOutCommands.setUnits(_G)
_CiscoScsiIntrPrtWrMegaBytes_Type=Counter32
_CiscoScsiIntrPrtWrMegaBytes_Object=MibTableColumn
ciscoScsiIntrPrtWrMegaBytes=_CiscoScsiIntrPrtWrMegaBytes_Object((1,3,6,1,4,1,9,10,95,1,3,3,1,4),_CiscoScsiIntrPrtWrMegaBytes_Type())
ciscoScsiIntrPrtWrMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiIntrPrtWrMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiIntrPrtWrMegaBytes.setUnits(_H)
_CiscoScsiIntrPrtReadMegaBytes_Type=Counter32
_CiscoScsiIntrPrtReadMegaBytes_Object=MibTableColumn
ciscoScsiIntrPrtReadMegaBytes=_CiscoScsiIntrPrtReadMegaBytes_Object((1,3,6,1,4,1,9,10,95,1,3,3,1,5),_CiscoScsiIntrPrtReadMegaBytes_Type())
ciscoScsiIntrPrtReadMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiIntrPrtReadMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiIntrPrtReadMegaBytes.setUnits(_H)
_CiscoScsiIntrPrtHSOutCommands_Type=Counter64
_CiscoScsiIntrPrtHSOutCommands_Object=MibTableColumn
ciscoScsiIntrPrtHSOutCommands=_CiscoScsiIntrPrtHSOutCommands_Object((1,3,6,1,4,1,9,10,95,1,3,3,1,6),_CiscoScsiIntrPrtHSOutCommands_Type())
ciscoScsiIntrPrtHSOutCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiIntrPrtHSOutCommands.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiIntrPrtHSOutCommands.setUnits(_G)
_CiscoScsiRemoteTarget_ObjectIdentity=ObjectIdentity
ciscoScsiRemoteTarget=_CiscoScsiRemoteTarget_ObjectIdentity((1,3,6,1,4,1,9,10,95,1,3,4))
_CiscoScsiDscTgtTable_Object=MibTable
ciscoScsiDscTgtTable=_CiscoScsiDscTgtTable_Object((1,3,6,1,4,1,9,10,95,1,3,4,1))
if mibBuilder.loadTexts:ciscoScsiDscTgtTable.setStatus(_A)
_CiscoScsiDscTgtEntry_Object=MibTableRow
ciscoScsiDscTgtEntry=_CiscoScsiDscTgtEntry_Object((1,3,6,1,4,1,9,10,95,1,3,4,1,1))
ciscoScsiDscTgtEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:ciscoScsiDscTgtEntry.setStatus(_A)
_CiscoScsiDscTgtIntrPortIndex_Type=ScsiPortIndexValueOrZero
_CiscoScsiDscTgtIntrPortIndex_Object=MibTableColumn
ciscoScsiDscTgtIntrPortIndex=_CiscoScsiDscTgtIntrPortIndex_Object((1,3,6,1,4,1,9,10,95,1,3,4,1,1,1),_CiscoScsiDscTgtIntrPortIndex_Type())
ciscoScsiDscTgtIntrPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiDscTgtIntrPortIndex.setStatus(_A)
_CiscoScsiDscTgtIndex_Type=ScsiIndexValue
_CiscoScsiDscTgtIndex_Object=MibTableColumn
ciscoScsiDscTgtIndex=_CiscoScsiDscTgtIndex_Object((1,3,6,1,4,1,9,10,95,1,3,4,1,1,2),_CiscoScsiDscTgtIndex_Type())
ciscoScsiDscTgtIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiDscTgtIndex.setStatus(_A)
_CiscoScsiDscTgtDevOrPort_Type=ScsiDeviceOrPort
_CiscoScsiDscTgtDevOrPort_Object=MibTableColumn
ciscoScsiDscTgtDevOrPort=_CiscoScsiDscTgtDevOrPort_Object((1,3,6,1,4,1,9,10,95,1,3,4,1,1,3),_CiscoScsiDscTgtDevOrPort_Type())
ciscoScsiDscTgtDevOrPort.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoScsiDscTgtDevOrPort.setStatus(_A)
_CiscoScsiDscTgtName_Type=ScsiName
_CiscoScsiDscTgtName_Object=MibTableColumn
ciscoScsiDscTgtName=_CiscoScsiDscTgtName_Object((1,3,6,1,4,1,9,10,95,1,3,4,1,1,4),_CiscoScsiDscTgtName_Type())
ciscoScsiDscTgtName.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoScsiDscTgtName.setStatus(_A)
class _CiscoScsiDscTgtConfigured_Type(TruthValue):defaultValue=1
_CiscoScsiDscTgtConfigured_Type.__name__=_Q
_CiscoScsiDscTgtConfigured_Object=MibTableColumn
ciscoScsiDscTgtConfigured=_CiscoScsiDscTgtConfigured_Object((1,3,6,1,4,1,9,10,95,1,3,4,1,1,5),_CiscoScsiDscTgtConfigured_Type())
ciscoScsiDscTgtConfigured.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoScsiDscTgtConfigured.setStatus(_A)
_CiscoScsiDscTgtDiscovered_Type=TruthValue
_CiscoScsiDscTgtDiscovered_Object=MibTableColumn
ciscoScsiDscTgtDiscovered=_CiscoScsiDscTgtDiscovered_Object((1,3,6,1,4,1,9,10,95,1,3,4,1,1,6),_CiscoScsiDscTgtDiscovered_Type())
ciscoScsiDscTgtDiscovered.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDscTgtDiscovered.setStatus(_A)
_CiscoScsiDscTgtInCommands_Type=Counter32
_CiscoScsiDscTgtInCommands_Object=MibTableColumn
ciscoScsiDscTgtInCommands=_CiscoScsiDscTgtInCommands_Object((1,3,6,1,4,1,9,10,95,1,3,4,1,1,7),_CiscoScsiDscTgtInCommands_Type())
ciscoScsiDscTgtInCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDscTgtInCommands.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiDscTgtInCommands.setUnits(_G)
_CiscoScsiDscTgtWrMegaBytes_Type=Counter32
_CiscoScsiDscTgtWrMegaBytes_Object=MibTableColumn
ciscoScsiDscTgtWrMegaBytes=_CiscoScsiDscTgtWrMegaBytes_Object((1,3,6,1,4,1,9,10,95,1,3,4,1,1,8),_CiscoScsiDscTgtWrMegaBytes_Type())
ciscoScsiDscTgtWrMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDscTgtWrMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiDscTgtWrMegaBytes.setUnits(_H)
_CiscoScsiDscTgtReadMegaBytes_Type=Counter32
_CiscoScsiDscTgtReadMegaBytes_Object=MibTableColumn
ciscoScsiDscTgtReadMegaBytes=_CiscoScsiDscTgtReadMegaBytes_Object((1,3,6,1,4,1,9,10,95,1,3,4,1,1,9),_CiscoScsiDscTgtReadMegaBytes_Type())
ciscoScsiDscTgtReadMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDscTgtReadMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiDscTgtReadMegaBytes.setUnits(_H)
_CiscoScsiDscTgtHSInCommands_Type=Counter64
_CiscoScsiDscTgtHSInCommands_Object=MibTableColumn
ciscoScsiDscTgtHSInCommands=_CiscoScsiDscTgtHSInCommands_Object((1,3,6,1,4,1,9,10,95,1,3,4,1,1,10),_CiscoScsiDscTgtHSInCommands_Type())
ciscoScsiDscTgtHSInCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDscTgtHSInCommands.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiDscTgtHSInCommands.setUnits(_G)
_CiscoScsiDscTgtLastCreation_Type=TimeStamp
_CiscoScsiDscTgtLastCreation_Object=MibTableColumn
ciscoScsiDscTgtLastCreation=_CiscoScsiDscTgtLastCreation_Object((1,3,6,1,4,1,9,10,95,1,3,4,1,1,11),_CiscoScsiDscTgtLastCreation_Type())
ciscoScsiDscTgtLastCreation.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDscTgtLastCreation.setStatus(_A)
_CiscoScsiDscTgtRowStatus_Type=RowStatus
_CiscoScsiDscTgtRowStatus_Object=MibTableColumn
ciscoScsiDscTgtRowStatus=_CiscoScsiDscTgtRowStatus_Object((1,3,6,1,4,1,9,10,95,1,3,4,1,1,12),_CiscoScsiDscTgtRowStatus_Type())
ciscoScsiDscTgtRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoScsiDscTgtRowStatus.setStatus(_A)
_CiscoScsiDscLunTable_Object=MibTable
ciscoScsiDscLunTable=_CiscoScsiDscLunTable_Object((1,3,6,1,4,1,9,10,95,1,3,4,2))
if mibBuilder.loadTexts:ciscoScsiDscLunTable.setStatus(_A)
_CiscoScsiDscLunEntry_Object=MibTableRow
ciscoScsiDscLunEntry=_CiscoScsiDscLunEntry_Object((1,3,6,1,4,1,9,10,95,1,3,4,2,1))
ciscoScsiDscLunEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_O),(0,_B,_P),(0,_B,_S))
if mibBuilder.loadTexts:ciscoScsiDscLunEntry.setStatus(_A)
_CiscoScsiDscLunIndex_Type=ScsiIndexValue
_CiscoScsiDscLunIndex_Object=MibTableColumn
ciscoScsiDscLunIndex=_CiscoScsiDscLunIndex_Object((1,3,6,1,4,1,9,10,95,1,3,4,2,1,1),_CiscoScsiDscLunIndex_Type())
ciscoScsiDscLunIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiDscLunIndex.setStatus(_A)
_CiscoScsiDscLunLun_Type=ScsiLUNOrZero
_CiscoScsiDscLunLun_Object=MibTableColumn
ciscoScsiDscLunLun=_CiscoScsiDscLunLun_Object((1,3,6,1,4,1,9,10,95,1,3,4,2,1,2),_CiscoScsiDscLunLun_Type())
ciscoScsiDscLunLun.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDscLunLun.setStatus(_A)
_CiscoScsiDscLunIdTable_Object=MibTable
ciscoScsiDscLunIdTable=_CiscoScsiDscLunIdTable_Object((1,3,6,1,4,1,9,10,95,1,3,4,3))
if mibBuilder.loadTexts:ciscoScsiDscLunIdTable.setStatus(_A)
_CiscoScsiDscLunIdEntry_Object=MibTableRow
ciscoScsiDscLunIdEntry=_CiscoScsiDscLunIdEntry_Object((1,3,6,1,4,1,9,10,95,1,3,4,3,1))
ciscoScsiDscLunIdEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_O),(0,_B,_P),(0,_B,_S),(0,_B,_Z))
if mibBuilder.loadTexts:ciscoScsiDscLunIdEntry.setStatus(_A)
_CiscoScsiDscLunIdIndex_Type=ScsiIndexValue
_CiscoScsiDscLunIdIndex_Object=MibTableColumn
ciscoScsiDscLunIdIndex=_CiscoScsiDscLunIdIndex_Object((1,3,6,1,4,1,9,10,95,1,3,4,3,1,1),_CiscoScsiDscLunIdIndex_Type())
ciscoScsiDscLunIdIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiDscLunIdIndex.setStatus(_A)
_CiscoScsiDscLunIdCodeSet_Type=ScsiIdCodeSet
_CiscoScsiDscLunIdCodeSet_Object=MibTableColumn
ciscoScsiDscLunIdCodeSet=_CiscoScsiDscLunIdCodeSet_Object((1,3,6,1,4,1,9,10,95,1,3,4,3,1,2),_CiscoScsiDscLunIdCodeSet_Type())
ciscoScsiDscLunIdCodeSet.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDscLunIdCodeSet.setStatus(_A)
_CiscoScsiDscLunIdAssociation_Type=ScsiIdAssociation
_CiscoScsiDscLunIdAssociation_Object=MibTableColumn
ciscoScsiDscLunIdAssociation=_CiscoScsiDscLunIdAssociation_Object((1,3,6,1,4,1,9,10,95,1,3,4,3,1,3),_CiscoScsiDscLunIdAssociation_Type())
ciscoScsiDscLunIdAssociation.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDscLunIdAssociation.setStatus(_A)
_CiscoScsiDscLunIdType_Type=ScsiIdType
_CiscoScsiDscLunIdType_Object=MibTableColumn
ciscoScsiDscLunIdType=_CiscoScsiDscLunIdType_Object((1,3,6,1,4,1,9,10,95,1,3,4,3,1,4),_CiscoScsiDscLunIdType_Type())
ciscoScsiDscLunIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDscLunIdType.setStatus(_A)
_CiscoScsiDscLunIdValue_Type=ScsiIdValue
_CiscoScsiDscLunIdValue_Object=MibTableColumn
ciscoScsiDscLunIdValue=_CiscoScsiDscLunIdValue_Object((1,3,6,1,4,1,9,10,95,1,3,4,3,1,5),_CiscoScsiDscLunIdValue_Type())
ciscoScsiDscLunIdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiDscLunIdValue.setStatus(_A)
_CiscoScsiAttTgtPortTable_Object=MibTable
ciscoScsiAttTgtPortTable=_CiscoScsiAttTgtPortTable_Object((1,3,6,1,4,1,9,10,95,1,3,4,6))
if mibBuilder.loadTexts:ciscoScsiAttTgtPortTable.setStatus(_A)
_CiscoScsiAttTgtPortEntry_Object=MibTableRow
ciscoScsiAttTgtPortEntry=_CiscoScsiAttTgtPortEntry_Object((1,3,6,1,4,1,9,10,95,1,3,4,6,1))
ciscoScsiAttTgtPortEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_K),(0,_B,_a))
if mibBuilder.loadTexts:ciscoScsiAttTgtPortEntry.setStatus(_A)
_CiscoScsiAttTgtPortIndex_Type=ScsiIndexValue
_CiscoScsiAttTgtPortIndex_Object=MibTableColumn
ciscoScsiAttTgtPortIndex=_CiscoScsiAttTgtPortIndex_Object((1,3,6,1,4,1,9,10,95,1,3,4,6,1,1),_CiscoScsiAttTgtPortIndex_Type())
ciscoScsiAttTgtPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiAttTgtPortIndex.setStatus(_A)
_CiscoScsiAttTgtPortDscTgtIdx_Type=ScsiIndexValueOrZero
_CiscoScsiAttTgtPortDscTgtIdx_Object=MibTableColumn
ciscoScsiAttTgtPortDscTgtIdx=_CiscoScsiAttTgtPortDscTgtIdx_Object((1,3,6,1,4,1,9,10,95,1,3,4,6,1,2),_CiscoScsiAttTgtPortDscTgtIdx_Type())
ciscoScsiAttTgtPortDscTgtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiAttTgtPortDscTgtIdx.setStatus(_A)
_CiscoScsiAttTgtPortName_Type=ScsiName
_CiscoScsiAttTgtPortName_Object=MibTableColumn
ciscoScsiAttTgtPortName=_CiscoScsiAttTgtPortName_Object((1,3,6,1,4,1,9,10,95,1,3,4,6,1,3),_CiscoScsiAttTgtPortName_Type())
ciscoScsiAttTgtPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiAttTgtPortName.setStatus(_A)
_CiscoScsiAttTgtPortIdentifier_Type=ScsiIdentifier
_CiscoScsiAttTgtPortIdentifier_Object=MibTableColumn
ciscoScsiAttTgtPortIdentifier=_CiscoScsiAttTgtPortIdentifier_Object((1,3,6,1,4,1,9,10,95,1,3,4,6,1,4),_CiscoScsiAttTgtPortIdentifier_Type())
ciscoScsiAttTgtPortIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiAttTgtPortIdentifier.setStatus(_A)
_CiscoScsiTarget_ObjectIdentity=ObjectIdentity
ciscoScsiTarget=_CiscoScsiTarget_ObjectIdentity((1,3,6,1,4,1,9,10,95,1,4))
_CiscoScsiTgtDevTable_Object=MibTable
ciscoScsiTgtDevTable=_CiscoScsiTgtDevTable_Object((1,3,6,1,4,1,9,10,95,1,4,1))
if mibBuilder.loadTexts:ciscoScsiTgtDevTable.setStatus(_A)
_CiscoScsiTgtDevEntry_Object=MibTableRow
ciscoScsiTgtDevEntry=_CiscoScsiTgtDevEntry_Object((1,3,6,1,4,1,9,10,95,1,4,1,1))
ciscoScsiTgtDevEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:ciscoScsiTgtDevEntry.setStatus(_A)
_CiscoScsiTgtDevNumberOfLUs_Type=Gauge32
_CiscoScsiTgtDevNumberOfLUs_Object=MibTableColumn
ciscoScsiTgtDevNumberOfLUs=_CiscoScsiTgtDevNumberOfLUs_Object((1,3,6,1,4,1,9,10,95,1,4,1,1,1),_CiscoScsiTgtDevNumberOfLUs_Type())
ciscoScsiTgtDevNumberOfLUs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiTgtDevNumberOfLUs.setStatus(_A)
class _CiscoScsiTgtDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_R,1),(_b,2),(_c,3),(_d,4),(_e,5),('nonAddrFailure',6),('nonAddrFailReadying',7),('nonAddrFailAbnormal',8)))
_CiscoScsiTgtDeviceStatus_Type.__name__=_M
_CiscoScsiTgtDeviceStatus_Object=MibTableColumn
ciscoScsiTgtDeviceStatus=_CiscoScsiTgtDeviceStatus_Object((1,3,6,1,4,1,9,10,95,1,4,1,1,2),_CiscoScsiTgtDeviceStatus_Type())
ciscoScsiTgtDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiTgtDeviceStatus.setStatus(_A)
_CiscoScsiTgtDevNonAccLUs_Type=Gauge32
_CiscoScsiTgtDevNonAccLUs_Object=MibTableColumn
ciscoScsiTgtDevNonAccLUs=_CiscoScsiTgtDevNonAccLUs_Object((1,3,6,1,4,1,9,10,95,1,4,1,1,3),_CiscoScsiTgtDevNonAccLUs_Type())
ciscoScsiTgtDevNonAccLUs.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiTgtDevNonAccLUs.setStatus(_A)
_CiscoScsiTgtPortTable_Object=MibTable
ciscoScsiTgtPortTable=_CiscoScsiTgtPortTable_Object((1,3,6,1,4,1,9,10,95,1,4,2))
if mibBuilder.loadTexts:ciscoScsiTgtPortTable.setStatus(_A)
_CiscoScsiTgtPortEntry_Object=MibTableRow
ciscoScsiTgtPortEntry=_CiscoScsiTgtPortEntry_Object((1,3,6,1,4,1,9,10,95,1,4,2,1))
ciscoScsiTgtPortEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_K))
if mibBuilder.loadTexts:ciscoScsiTgtPortEntry.setStatus(_A)
_CiscoScsiTgtPortName_Type=ScsiName
_CiscoScsiTgtPortName_Object=MibTableColumn
ciscoScsiTgtPortName=_CiscoScsiTgtPortName_Object((1,3,6,1,4,1,9,10,95,1,4,2,1,1),_CiscoScsiTgtPortName_Type())
ciscoScsiTgtPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiTgtPortName.setStatus(_A)
_CiscoScsiTgtPortIdentifier_Type=ScsiIdentifier
_CiscoScsiTgtPortIdentifier_Object=MibTableColumn
ciscoScsiTgtPortIdentifier=_CiscoScsiTgtPortIdentifier_Object((1,3,6,1,4,1,9,10,95,1,4,2,1,2),_CiscoScsiTgtPortIdentifier_Type())
ciscoScsiTgtPortIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiTgtPortIdentifier.setStatus(_A)
_CiscoScsiTgtPortInCommands_Type=Counter32
_CiscoScsiTgtPortInCommands_Object=MibTableColumn
ciscoScsiTgtPortInCommands=_CiscoScsiTgtPortInCommands_Object((1,3,6,1,4,1,9,10,95,1,4,2,1,3),_CiscoScsiTgtPortInCommands_Type())
ciscoScsiTgtPortInCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiTgtPortInCommands.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiTgtPortInCommands.setUnits(_G)
_CiscoScsiTgtPortWrMegaBytes_Type=Counter32
_CiscoScsiTgtPortWrMegaBytes_Object=MibTableColumn
ciscoScsiTgtPortWrMegaBytes=_CiscoScsiTgtPortWrMegaBytes_Object((1,3,6,1,4,1,9,10,95,1,4,2,1,4),_CiscoScsiTgtPortWrMegaBytes_Type())
ciscoScsiTgtPortWrMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiTgtPortWrMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiTgtPortWrMegaBytes.setUnits(_H)
_CiscoScsiTgtPortReadMegaBytes_Type=Counter32
_CiscoScsiTgtPortReadMegaBytes_Object=MibTableColumn
ciscoScsiTgtPortReadMegaBytes=_CiscoScsiTgtPortReadMegaBytes_Object((1,3,6,1,4,1,9,10,95,1,4,2,1,5),_CiscoScsiTgtPortReadMegaBytes_Type())
ciscoScsiTgtPortReadMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiTgtPortReadMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiTgtPortReadMegaBytes.setUnits(_H)
_CiscoScsiTgtPortHSInCommands_Type=Counter64
_CiscoScsiTgtPortHSInCommands_Object=MibTableColumn
ciscoScsiTgtPortHSInCommands=_CiscoScsiTgtPortHSInCommands_Object((1,3,6,1,4,1,9,10,95,1,4,2,1,6),_CiscoScsiTgtPortHSInCommands_Type())
ciscoScsiTgtPortHSInCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiTgtPortHSInCommands.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiTgtPortHSInCommands.setUnits(_G)
_CiscoScsiRemoteInitiators_ObjectIdentity=ObjectIdentity
ciscoScsiRemoteInitiators=_CiscoScsiRemoteInitiators_ObjectIdentity((1,3,6,1,4,1,9,10,95,1,4,3))
_CiscoScsiAuthorizedIntrTable_Object=MibTable
ciscoScsiAuthorizedIntrTable=_CiscoScsiAuthorizedIntrTable_Object((1,3,6,1,4,1,9,10,95,1,4,3,1))
if mibBuilder.loadTexts:ciscoScsiAuthorizedIntrTable.setStatus(_A)
_CiscoScsiAuthorizedIntrEntry_Object=MibTableRow
ciscoScsiAuthorizedIntrEntry=_CiscoScsiAuthorizedIntrEntry_Object((1,3,6,1,4,1,9,10,95,1,4,3,1,1))
ciscoScsiAuthorizedIntrEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:ciscoScsiAuthorizedIntrEntry.setStatus(_A)
_CiscoScsiAuthIntrTgtPortIndex_Type=ScsiPortIndexValueOrZero
_CiscoScsiAuthIntrTgtPortIndex_Object=MibTableColumn
ciscoScsiAuthIntrTgtPortIndex=_CiscoScsiAuthIntrTgtPortIndex_Object((1,3,6,1,4,1,9,10,95,1,4,3,1,1,1),_CiscoScsiAuthIntrTgtPortIndex_Type())
ciscoScsiAuthIntrTgtPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiAuthIntrTgtPortIndex.setStatus(_A)
_CiscoScsiAuthIntrIndex_Type=ScsiIndexValue
_CiscoScsiAuthIntrIndex_Object=MibTableColumn
ciscoScsiAuthIntrIndex=_CiscoScsiAuthIntrIndex_Object((1,3,6,1,4,1,9,10,95,1,4,3,1,1,2),_CiscoScsiAuthIntrIndex_Type())
ciscoScsiAuthIntrIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiAuthIntrIndex.setStatus(_A)
_CiscoScsiAuthIntrDevOrPort_Type=ScsiDeviceOrPort
_CiscoScsiAuthIntrDevOrPort_Object=MibTableColumn
ciscoScsiAuthIntrDevOrPort=_CiscoScsiAuthIntrDevOrPort_Object((1,3,6,1,4,1,9,10,95,1,4,3,1,1,3),_CiscoScsiAuthIntrDevOrPort_Type())
ciscoScsiAuthIntrDevOrPort.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoScsiAuthIntrDevOrPort.setStatus(_A)
_CiscoScsiAuthIntrName_Type=ScsiName
_CiscoScsiAuthIntrName_Object=MibTableColumn
ciscoScsiAuthIntrName=_CiscoScsiAuthIntrName_Object((1,3,6,1,4,1,9,10,95,1,4,3,1,1,4),_CiscoScsiAuthIntrName_Type())
ciscoScsiAuthIntrName.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoScsiAuthIntrName.setStatus(_A)
_CiscoScsiAuthIntrLunMapIndex_Type=ScsiIndexValueOrZero
_CiscoScsiAuthIntrLunMapIndex_Object=MibTableColumn
ciscoScsiAuthIntrLunMapIndex=_CiscoScsiAuthIntrLunMapIndex_Object((1,3,6,1,4,1,9,10,95,1,4,3,1,1,5),_CiscoScsiAuthIntrLunMapIndex_Type())
ciscoScsiAuthIntrLunMapIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoScsiAuthIntrLunMapIndex.setStatus(_A)
_CiscoScsiAuthIntrAttachedTimes_Type=Counter32
_CiscoScsiAuthIntrAttachedTimes_Object=MibTableColumn
ciscoScsiAuthIntrAttachedTimes=_CiscoScsiAuthIntrAttachedTimes_Object((1,3,6,1,4,1,9,10,95,1,4,3,1,1,6),_CiscoScsiAuthIntrAttachedTimes_Type())
ciscoScsiAuthIntrAttachedTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiAuthIntrAttachedTimes.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiAuthIntrAttachedTimes.setUnits('Times')
_CiscoScsiAuthIntrOutCommands_Type=Counter32
_CiscoScsiAuthIntrOutCommands_Object=MibTableColumn
ciscoScsiAuthIntrOutCommands=_CiscoScsiAuthIntrOutCommands_Object((1,3,6,1,4,1,9,10,95,1,4,3,1,1,7),_CiscoScsiAuthIntrOutCommands_Type())
ciscoScsiAuthIntrOutCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiAuthIntrOutCommands.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiAuthIntrOutCommands.setUnits(_G)
_CiscoScsiAuthIntrReadMegaBytes_Type=Counter32
_CiscoScsiAuthIntrReadMegaBytes_Object=MibTableColumn
ciscoScsiAuthIntrReadMegaBytes=_CiscoScsiAuthIntrReadMegaBytes_Object((1,3,6,1,4,1,9,10,95,1,4,3,1,1,8),_CiscoScsiAuthIntrReadMegaBytes_Type())
ciscoScsiAuthIntrReadMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiAuthIntrReadMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiAuthIntrReadMegaBytes.setUnits(_H)
_CiscoScsiAuthIntrWrMegaBytes_Type=Counter32
_CiscoScsiAuthIntrWrMegaBytes_Object=MibTableColumn
ciscoScsiAuthIntrWrMegaBytes=_CiscoScsiAuthIntrWrMegaBytes_Object((1,3,6,1,4,1,9,10,95,1,4,3,1,1,9),_CiscoScsiAuthIntrWrMegaBytes_Type())
ciscoScsiAuthIntrWrMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiAuthIntrWrMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiAuthIntrWrMegaBytes.setUnits(_H)
_CiscoScsiAuthIntrHSOutCommands_Type=Counter64
_CiscoScsiAuthIntrHSOutCommands_Object=MibTableColumn
ciscoScsiAuthIntrHSOutCommands=_CiscoScsiAuthIntrHSOutCommands_Object((1,3,6,1,4,1,9,10,95,1,4,3,1,1,10),_CiscoScsiAuthIntrHSOutCommands_Type())
ciscoScsiAuthIntrHSOutCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiAuthIntrHSOutCommands.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiAuthIntrHSOutCommands.setUnits(_G)
_CiscoScsiAuthIntrLastCreation_Type=TimeStamp
_CiscoScsiAuthIntrLastCreation_Object=MibTableColumn
ciscoScsiAuthIntrLastCreation=_CiscoScsiAuthIntrLastCreation_Object((1,3,6,1,4,1,9,10,95,1,4,3,1,1,11),_CiscoScsiAuthIntrLastCreation_Type())
ciscoScsiAuthIntrLastCreation.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiAuthIntrLastCreation.setStatus(_A)
_CiscoScsiAuthIntrRowStatus_Type=RowStatus
_CiscoScsiAuthIntrRowStatus_Object=MibTableColumn
ciscoScsiAuthIntrRowStatus=_CiscoScsiAuthIntrRowStatus_Object((1,3,6,1,4,1,9,10,95,1,4,3,1,1,12),_CiscoScsiAuthIntrRowStatus_Type())
ciscoScsiAuthIntrRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoScsiAuthIntrRowStatus.setStatus(_A)
_CiscoScsiAttIntrPrtTable_Object=MibTable
ciscoScsiAttIntrPrtTable=_CiscoScsiAttIntrPrtTable_Object((1,3,6,1,4,1,9,10,95,1,4,3,2))
if mibBuilder.loadTexts:ciscoScsiAttIntrPrtTable.setStatus(_A)
_CiscoScsiAttIntrPrtEntry_Object=MibTableRow
ciscoScsiAttIntrPrtEntry=_CiscoScsiAttIntrPrtEntry_Object((1,3,6,1,4,1,9,10,95,1,4,3,2,1))
ciscoScsiAttIntrPrtEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_K),(0,_B,_h))
if mibBuilder.loadTexts:ciscoScsiAttIntrPrtEntry.setStatus(_A)
_CiscoScsiAttIntrPrtIdx_Type=ScsiIndexValue
_CiscoScsiAttIntrPrtIdx_Object=MibTableColumn
ciscoScsiAttIntrPrtIdx=_CiscoScsiAttIntrPrtIdx_Object((1,3,6,1,4,1,9,10,95,1,4,3,2,1,1),_CiscoScsiAttIntrPrtIdx_Type())
ciscoScsiAttIntrPrtIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiAttIntrPrtIdx.setStatus(_A)
_CiscoScsiAttIntrPrtAuthIntrIdx_Type=ScsiIndexValueOrZero
_CiscoScsiAttIntrPrtAuthIntrIdx_Object=MibTableColumn
ciscoScsiAttIntrPrtAuthIntrIdx=_CiscoScsiAttIntrPrtAuthIntrIdx_Object((1,3,6,1,4,1,9,10,95,1,4,3,2,1,2),_CiscoScsiAttIntrPrtAuthIntrIdx_Type())
ciscoScsiAttIntrPrtAuthIntrIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiAttIntrPrtAuthIntrIdx.setStatus(_A)
_CiscoScsiAttIntrPrtName_Type=ScsiName
_CiscoScsiAttIntrPrtName_Object=MibTableColumn
ciscoScsiAttIntrPrtName=_CiscoScsiAttIntrPrtName_Object((1,3,6,1,4,1,9,10,95,1,4,3,2,1,3),_CiscoScsiAttIntrPrtName_Type())
ciscoScsiAttIntrPrtName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiAttIntrPrtName.setStatus(_A)
_CiscoScsiAttIntrPrtId_Type=ScsiIdentifier
_CiscoScsiAttIntrPrtId_Object=MibTableColumn
ciscoScsiAttIntrPrtId=_CiscoScsiAttIntrPrtId_Object((1,3,6,1,4,1,9,10,95,1,4,3,2,1,4),_CiscoScsiAttIntrPrtId_Type())
ciscoScsiAttIntrPrtId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiAttIntrPrtId.setStatus(_A)
_CiscoScsiLogicalUnit_ObjectIdentity=ObjectIdentity
ciscoScsiLogicalUnit=_CiscoScsiLogicalUnit_ObjectIdentity((1,3,6,1,4,1,9,10,95,1,5))
_CiscoScsiLuTable_Object=MibTable
ciscoScsiLuTable=_CiscoScsiLuTable_Object((1,3,6,1,4,1,9,10,95,1,5,1))
if mibBuilder.loadTexts:ciscoScsiLuTable.setStatus(_A)
_CiscoScsiLuEntry_Object=MibTableRow
ciscoScsiLuEntry=_CiscoScsiLuEntry_Object((1,3,6,1,4,1,9,10,95,1,5,1,1))
ciscoScsiLuEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_T))
if mibBuilder.loadTexts:ciscoScsiLuEntry.setStatus(_A)
_CiscoScsiLuIndex_Type=ScsiIndexValue
_CiscoScsiLuIndex_Object=MibTableColumn
ciscoScsiLuIndex=_CiscoScsiLuIndex_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,1),_CiscoScsiLuIndex_Type())
ciscoScsiLuIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiLuIndex.setStatus(_A)
_CiscoScsiLuDefaultLun_Type=ScsiLUNOrZero
_CiscoScsiLuDefaultLun_Object=MibTableColumn
ciscoScsiLuDefaultLun=_CiscoScsiLuDefaultLun_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,2),_CiscoScsiLuDefaultLun_Type())
ciscoScsiLuDefaultLun.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuDefaultLun.setStatus(_A)
_CiscoScsiLuWwnName_Type=ScsiNameIdOrZero
_CiscoScsiLuWwnName_Object=MibTableColumn
ciscoScsiLuWwnName=_CiscoScsiLuWwnName_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,3),_CiscoScsiLuWwnName_Type())
ciscoScsiLuWwnName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuWwnName.setStatus(_A)
class _CiscoScsiLuVendorId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_CiscoScsiLuVendorId_Type.__name__=_J
_CiscoScsiLuVendorId_Object=MibTableColumn
ciscoScsiLuVendorId=_CiscoScsiLuVendorId_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,4),_CiscoScsiLuVendorId_Type())
ciscoScsiLuVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuVendorId.setStatus(_A)
class _CiscoScsiLuProductId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_CiscoScsiLuProductId_Type.__name__=_J
_CiscoScsiLuProductId_Object=MibTableColumn
ciscoScsiLuProductId=_CiscoScsiLuProductId_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,5),_CiscoScsiLuProductId_Type())
ciscoScsiLuProductId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuProductId.setStatus(_A)
class _CiscoScsiLuRevisionId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_CiscoScsiLuRevisionId_Type.__name__=_J
_CiscoScsiLuRevisionId_Object=MibTableColumn
ciscoScsiLuRevisionId=_CiscoScsiLuRevisionId_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,6),_CiscoScsiLuRevisionId_Type())
ciscoScsiLuRevisionId.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuRevisionId.setStatus(_A)
_CiscoScsiLuPeripheralType_Type=Unsigned32
_CiscoScsiLuPeripheralType_Object=MibTableColumn
ciscoScsiLuPeripheralType=_CiscoScsiLuPeripheralType_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,7),_CiscoScsiLuPeripheralType_Type())
ciscoScsiLuPeripheralType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuPeripheralType.setStatus(_A)
class _CiscoScsiLuStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_R,1),(_b,2),('notAvailable',3),(_c,4),(_d,5),(_e,6)))
_CiscoScsiLuStatus_Type.__name__=_M
_CiscoScsiLuStatus_Object=MibTableColumn
ciscoScsiLuStatus=_CiscoScsiLuStatus_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,8),_CiscoScsiLuStatus_Type())
ciscoScsiLuStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuStatus.setStatus(_A)
class _CiscoScsiLuState_Type(Bits):namedValues=NamedValues(*(('dataLost',0),('dynamicReconfigurationInProgress',1),('exposed',2),('fractionallyExposed',3),('partiallyExposed',4),('protectedRebuild',5),('protectionDisabled',6),('rebuild',7),('recalculate',8),('spareInUse',9),('verifyInProgress',10)))
_CiscoScsiLuState_Type.__name__=_L
_CiscoScsiLuState_Object=MibTableColumn
ciscoScsiLuState=_CiscoScsiLuState_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,9),_CiscoScsiLuState_Type())
ciscoScsiLuState.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuState.setStatus(_A)
_CiscoScsiLuInCommands_Type=Counter32
_CiscoScsiLuInCommands_Object=MibTableColumn
ciscoScsiLuInCommands=_CiscoScsiLuInCommands_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,10),_CiscoScsiLuInCommands_Type())
ciscoScsiLuInCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuInCommands.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiLuInCommands.setUnits(_G)
_CiscoScsiLuReadMegaBytes_Type=Counter32
_CiscoScsiLuReadMegaBytes_Object=MibTableColumn
ciscoScsiLuReadMegaBytes=_CiscoScsiLuReadMegaBytes_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,11),_CiscoScsiLuReadMegaBytes_Type())
ciscoScsiLuReadMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuReadMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiLuReadMegaBytes.setUnits(_H)
_CiscoScsiLuWrittenMegaBytes_Type=Counter32
_CiscoScsiLuWrittenMegaBytes_Object=MibTableColumn
ciscoScsiLuWrittenMegaBytes=_CiscoScsiLuWrittenMegaBytes_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,12),_CiscoScsiLuWrittenMegaBytes_Type())
ciscoScsiLuWrittenMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuWrittenMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiLuWrittenMegaBytes.setUnits(_H)
_CiscoScsiLuInResets_Type=Counter32
_CiscoScsiLuInResets_Object=MibTableColumn
ciscoScsiLuInResets=_CiscoScsiLuInResets_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,13),_CiscoScsiLuInResets_Type())
ciscoScsiLuInResets.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuInResets.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiLuInResets.setUnits('resets')
_CiscoScsiLuOutQueueFullStatus_Type=Counter32
_CiscoScsiLuOutQueueFullStatus_Object=MibTableColumn
ciscoScsiLuOutQueueFullStatus=_CiscoScsiLuOutQueueFullStatus_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,14),_CiscoScsiLuOutQueueFullStatus_Type())
ciscoScsiLuOutQueueFullStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuOutQueueFullStatus.setStatus(_A)
_CiscoScsiLuHSInCommands_Type=Counter64
_CiscoScsiLuHSInCommands_Object=MibTableColumn
ciscoScsiLuHSInCommands=_CiscoScsiLuHSInCommands_Object((1,3,6,1,4,1,9,10,95,1,5,1,1,15),_CiscoScsiLuHSInCommands_Type())
ciscoScsiLuHSInCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuHSInCommands.setStatus(_A)
if mibBuilder.loadTexts:ciscoScsiLuHSInCommands.setUnits(_G)
_CiscoScsiLuIdTable_Object=MibTable
ciscoScsiLuIdTable=_CiscoScsiLuIdTable_Object((1,3,6,1,4,1,9,10,95,1,5,2))
if mibBuilder.loadTexts:ciscoScsiLuIdTable.setStatus(_A)
_CiscoScsiLuIdEntry_Object=MibTableRow
ciscoScsiLuIdEntry=_CiscoScsiLuIdEntry_Object((1,3,6,1,4,1,9,10,95,1,5,2,1))
ciscoScsiLuIdEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_T),(0,_B,_i))
if mibBuilder.loadTexts:ciscoScsiLuIdEntry.setStatus(_A)
_CiscoScsiLuIdIndex_Type=ScsiIndexValue
_CiscoScsiLuIdIndex_Object=MibTableColumn
ciscoScsiLuIdIndex=_CiscoScsiLuIdIndex_Object((1,3,6,1,4,1,9,10,95,1,5,2,1,1),_CiscoScsiLuIdIndex_Type())
ciscoScsiLuIdIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiLuIdIndex.setStatus(_A)
_CiscoScsiLuIdCodeSet_Type=ScsiIdCodeSet
_CiscoScsiLuIdCodeSet_Object=MibTableColumn
ciscoScsiLuIdCodeSet=_CiscoScsiLuIdCodeSet_Object((1,3,6,1,4,1,9,10,95,1,5,2,1,2),_CiscoScsiLuIdCodeSet_Type())
ciscoScsiLuIdCodeSet.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuIdCodeSet.setStatus(_A)
_CiscoScsiLuIdAssociation_Type=ScsiIdAssociation
_CiscoScsiLuIdAssociation_Object=MibTableColumn
ciscoScsiLuIdAssociation=_CiscoScsiLuIdAssociation_Object((1,3,6,1,4,1,9,10,95,1,5,2,1,3),_CiscoScsiLuIdAssociation_Type())
ciscoScsiLuIdAssociation.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuIdAssociation.setStatus(_A)
_CiscoScsiLuIdType_Type=ScsiIdType
_CiscoScsiLuIdType_Object=MibTableColumn
ciscoScsiLuIdType=_CiscoScsiLuIdType_Object((1,3,6,1,4,1,9,10,95,1,5,2,1,4),_CiscoScsiLuIdType_Type())
ciscoScsiLuIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuIdType.setStatus(_A)
_CiscoScsiLuIdValue_Type=ScsiIdValue
_CiscoScsiLuIdValue_Object=MibTableColumn
ciscoScsiLuIdValue=_CiscoScsiLuIdValue_Object((1,3,6,1,4,1,9,10,95,1,5,2,1,5),_CiscoScsiLuIdValue_Type())
ciscoScsiLuIdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ciscoScsiLuIdValue.setStatus(_A)
_CiscoScsiLunMapTable_Object=MibTable
ciscoScsiLunMapTable=_CiscoScsiLunMapTable_Object((1,3,6,1,4,1,9,10,95,1,5,3))
if mibBuilder.loadTexts:ciscoScsiLunMapTable.setStatus(_A)
_CiscoScsiLunMapEntry_Object=MibTableRow
ciscoScsiLunMapEntry=_CiscoScsiLunMapEntry_Object((1,3,6,1,4,1,9,10,95,1,5,3,1))
ciscoScsiLunMapEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_j),(0,_B,_k))
if mibBuilder.loadTexts:ciscoScsiLunMapEntry.setStatus(_A)
_CiscoScsiLunMapIndex_Type=ScsiIndexValue
_CiscoScsiLunMapIndex_Object=MibTableColumn
ciscoScsiLunMapIndex=_CiscoScsiLunMapIndex_Object((1,3,6,1,4,1,9,10,95,1,5,3,1,1),_CiscoScsiLunMapIndex_Type())
ciscoScsiLunMapIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiLunMapIndex.setStatus(_A)
_CiscoScsiLunMapLun_Type=ScsiLUNOrZero
_CiscoScsiLunMapLun_Object=MibTableColumn
ciscoScsiLunMapLun=_CiscoScsiLunMapLun_Object((1,3,6,1,4,1,9,10,95,1,5,3,1,2),_CiscoScsiLunMapLun_Type())
ciscoScsiLunMapLun.setMaxAccess(_F)
if mibBuilder.loadTexts:ciscoScsiLunMapLun.setStatus(_A)
_CiscoScsiLunMapLuIndex_Type=ScsiIndexValue
_CiscoScsiLunMapLuIndex_Object=MibTableColumn
ciscoScsiLunMapLuIndex=_CiscoScsiLunMapLuIndex_Object((1,3,6,1,4,1,9,10,95,1,5,3,1,3),_CiscoScsiLunMapLuIndex_Type())
ciscoScsiLunMapLuIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoScsiLunMapLuIndex.setStatus(_A)
_CiscoScsiLunMapRowStatus_Type=RowStatus
_CiscoScsiLunMapRowStatus_Object=MibTableColumn
ciscoScsiLunMapRowStatus=_CiscoScsiLunMapRowStatus_Object((1,3,6,1,4,1,9,10,95,1,5,3,1,4),_CiscoScsiLunMapRowStatus_Type())
ciscoScsiLunMapRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:ciscoScsiLunMapRowStatus.setStatus(_A)
_CiscoScsiNotification_ObjectIdentity=ObjectIdentity
ciscoScsiNotification=_CiscoScsiNotification_ObjectIdentity((1,3,6,1,4,1,9,10,95,2))
_CiscoScsiNotifications_ObjectIdentity=ObjectIdentity
ciscoScsiNotifications=_CiscoScsiNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,95,2,0))
_CiscoScsiConformance_ObjectIdentity=ObjectIdentity
ciscoScsiConformance=_CiscoScsiConformance_ObjectIdentity((1,3,6,1,4,1,9,10,95,3))
_CiscoScsiCompliances_ObjectIdentity=ObjectIdentity
ciscoScsiCompliances=_CiscoScsiCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,95,3,1))
_CiscoScsiGroups_ObjectIdentity=ObjectIdentity
ciscoScsiGroups=_CiscoScsiGroups_ObjectIdentity((1,3,6,1,4,1,9,10,95,3,2))
ciscoScsiDeviceGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,1))
ciscoScsiDeviceGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:ciscoScsiDeviceGroup.setStatus(_A)
ciscoScsiInitiatorGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,2))
ciscoScsiInitiatorGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:ciscoScsiInitiatorGroup.setStatus(_A)
ciscoScsiDiscoveryGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,3))
ciscoScsiDiscoveryGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:ciscoScsiDiscoveryGroup.setStatus(_A)
ciscoScsiTargetGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,4))
ciscoScsiTargetGroup.setObjects(*((_B,_AE),(_B,_U),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_V),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:ciscoScsiTargetGroup.setStatus(_A)
ciscoScsiLunMapGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,5))
ciscoScsiLunMapGroup.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:ciscoScsiLunMapGroup.setStatus(_A)
ciscoScsiTargetStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,6))
ciscoScsiTargetStatsGroup.setObjects(*((_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak)))
if mibBuilder.loadTexts:ciscoScsiTargetStatsGroup.setStatus(_A)
ciscoScsiTargetHSStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,7))
ciscoScsiTargetHSStatsGroup.setObjects(*((_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:ciscoScsiTargetHSStatsGroup.setStatus(_A)
ciscoScsiLunMapStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,8))
ciscoScsiLunMapStatsGroup.setObjects(*((_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq)))
if mibBuilder.loadTexts:ciscoScsiLunMapStatsGroup.setStatus(_A)
ciscoScsiLunMapHSStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,9))
ciscoScsiLunMapHSStatsGroup.setObjects((_B,_Ar))
if mibBuilder.loadTexts:ciscoScsiLunMapHSStatsGroup.setStatus(_A)
ciscoScsiInitiatorStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,10))
ciscoScsiInitiatorStatsGroup.setObjects(*((_B,_As),(_B,_At),(_B,_Au),(_B,_Av)))
if mibBuilder.loadTexts:ciscoScsiInitiatorStatsGroup.setStatus(_A)
ciscoScsiInitiatorHSStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,11))
ciscoScsiInitiatorHSStatsGroup.setObjects((_B,_Aw))
if mibBuilder.loadTexts:ciscoScsiInitiatorHSStatsGroup.setStatus(_A)
ciscoScsiDiscoveryStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,12))
ciscoScsiDiscoveryStatsGroup.setObjects(*((_B,_Ax),(_B,_Ay),(_B,_Az)))
if mibBuilder.loadTexts:ciscoScsiDiscoveryStatsGroup.setStatus(_A)
ciscoScsiDiscoveryHSStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,13))
ciscoScsiDiscoveryHSStatsGroup.setObjects((_B,_A_))
if mibBuilder.loadTexts:ciscoScsiDiscoveryHSStatsGroup.setStatus(_A)
ciscoScsiDeviceStatGroup=ObjectGroup((1,3,6,1,4,1,9,10,95,3,2,14))
ciscoScsiDeviceStatGroup.setObjects(*((_B,_B0),(_B,_B1)))
if mibBuilder.loadTexts:ciscoScsiDeviceStatGroup.setStatus(_A)
ciscoScsiTgtDevStatusChanged=NotificationType((1,3,6,1,4,1,9,10,95,2,0,1))
ciscoScsiTgtDevStatusChanged.setObjects((_B,_U))
if mibBuilder.loadTexts:ciscoScsiTgtDevStatusChanged.setStatus(_A)
ciscoScsiLuStatusChanged=NotificationType((1,3,6,1,4,1,9,10,95,2,0,2))
ciscoScsiLuStatusChanged.setObjects((_B,_V))
if mibBuilder.loadTexts:ciscoScsiLuStatusChanged.setStatus(_A)
ciscoScsiNotifGroup=NotificationGroup((1,3,6,1,4,1,9,10,95,3,2,15))
ciscoScsiNotifGroup.setObjects(*((_B,_B2),(_B,_B3)))
if mibBuilder.loadTexts:ciscoScsiNotifGroup.setStatus(_A)
ciscoScsiCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,95,3,1,1))
ciscoScsiCompliance.setObjects((_B,_B4))
if mibBuilder.loadTexts:ciscoScsiCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ScsiLUNOrZero':ScsiLUNOrZero,'ScsiIndexValue':ScsiIndexValue,'ScsiPortIndexValueOrZero':ScsiPortIndexValueOrZero,'ScsiIndexValueOrZero':ScsiIndexValueOrZero,'ScsiIdentifier':ScsiIdentifier,'ScsiName':ScsiName,'ScsiNameIdOrZero':ScsiNameIdOrZero,'ScsiDeviceOrPort':ScsiDeviceOrPort,'ScsiIdCodeSet':ScsiIdCodeSet,'ScsiIdAssociation':ScsiIdAssociation,'ScsiIdType':ScsiIdType,'ScsiIdValue':ScsiIdValue,'HrSWInstalledIndexOrZero':HrSWInstalledIndexOrZero,'ciscoScsiMIB':ciscoScsiMIB,'ciscoScsiObjects':ciscoScsiObjects,'ciscoScsiTransportTypes':ciscoScsiTransportTypes,'ciscoScsiTranportOther':ciscoScsiTranportOther,'ciscoScsiTranportSPI':ciscoScsiTranportSPI,'ciscoScsiTransportFCP':ciscoScsiTransportFCP,'ciscoScsiTransportSRP':ciscoScsiTransportSRP,'ciscoScsiTransportISCSI':ciscoScsiTransportISCSI,'ciscoScsiTransportSBP':ciscoScsiTransportSBP,'ciscoScsiGeneral':ciscoScsiGeneral,'ciscoScsiInstanceTable':ciscoScsiInstanceTable,'ciscoScsiInstanceEntry':ciscoScsiInstanceEntry,_D:ciscoScsiInstIndex,_l:ciscoScsiInstAlias,_m:ciscoScsiInstSoftwareIndex,_n:ciscoScsiInstVendorVersion,_o:ciscoScsiInstNotifEnable,'ciscoScsiDeviceTable':ciscoScsiDeviceTable,'ciscoScsiDeviceEntry':ciscoScsiDeviceEntry,_E:ciscoScsiDeviceIndex,_p:ciscoScsiDeviceAlias,_q:ciscoScsiDeviceRole,_r:ciscoScsiDevicePortNumber,_B0:ciscoScsiDeviceResets,'ciscoScsiPortTable':ciscoScsiPortTable,'ciscoScsiPortEntry':ciscoScsiPortEntry,_K:ciscoScsiPortIndex,_s:ciscoScsiPortRole,_t:ciscoScsiPortTrnsptPtr,_B1:ciscoScsiPortBusyStatuses,'ciscoScsiTrnsptTable':ciscoScsiTrnsptTable,'ciscoScsiTrnsptEntry':ciscoScsiTrnsptEntry,_Y:ciscoScsiTrnsptIndex,_u:ciscoScsiTrnsptType,_v:ciscoScsiTrnsptPointer,_w:ciscoScsiTrnsptDevName,'ciscoScsiInitiator':ciscoScsiInitiator,'ciscoScsiIntrDevTable':ciscoScsiIntrDevTable,'ciscoScsiIntrDevEntry':ciscoScsiIntrDevEntry,_x:ciscoScsiIntrDevAccMode,_As:ciscoScsiIntrDevOutResets,'ciscoScsiIntrPrtTable':ciscoScsiIntrPrtTable,'ciscoScsiIntrPrtEntry':ciscoScsiIntrPrtEntry,_y:ciscoScsiIntrPrtName,_z:ciscoScsiIntrPrtIdentifier,_At:ciscoScsiIntrPrtOutCommands,_Au:ciscoScsiIntrPrtWrMegaBytes,_Av:ciscoScsiIntrPrtReadMegaBytes,_Aw:ciscoScsiIntrPrtHSOutCommands,'ciscoScsiRemoteTarget':ciscoScsiRemoteTarget,'ciscoScsiDscTgtTable':ciscoScsiDscTgtTable,'ciscoScsiDscTgtEntry':ciscoScsiDscTgtEntry,_O:ciscoScsiDscTgtIntrPortIndex,_P:ciscoScsiDscTgtIndex,_A3:ciscoScsiDscTgtDevOrPort,_A4:ciscoScsiDscTgtName,_A5:ciscoScsiDscTgtConfigured,_A6:ciscoScsiDscTgtDiscovered,_Ax:ciscoScsiDscTgtInCommands,_Az:ciscoScsiDscTgtWrMegaBytes,_Ay:ciscoScsiDscTgtReadMegaBytes,_A_:ciscoScsiDscTgtHSInCommands,_A8:ciscoScsiDscTgtLastCreation,_A7:ciscoScsiDscTgtRowStatus,'ciscoScsiDscLunTable':ciscoScsiDscLunTable,'ciscoScsiDscLunEntry':ciscoScsiDscLunEntry,_S:ciscoScsiDscLunIndex,_A9:ciscoScsiDscLunLun,'ciscoScsiDscLunIdTable':ciscoScsiDscLunIdTable,'ciscoScsiDscLunIdEntry':ciscoScsiDscLunIdEntry,_Z:ciscoScsiDscLunIdIndex,_AA:ciscoScsiDscLunIdCodeSet,_AB:ciscoScsiDscLunIdAssociation,_AC:ciscoScsiDscLunIdType,_AD:ciscoScsiDscLunIdValue,'ciscoScsiAttTgtPortTable':ciscoScsiAttTgtPortTable,'ciscoScsiAttTgtPortEntry':ciscoScsiAttTgtPortEntry,_a:ciscoScsiAttTgtPortIndex,_A0:ciscoScsiAttTgtPortDscTgtIdx,_A1:ciscoScsiAttTgtPortName,_A2:ciscoScsiAttTgtPortIdentifier,'ciscoScsiTarget':ciscoScsiTarget,'ciscoScsiTgtDevTable':ciscoScsiTgtDevTable,'ciscoScsiTgtDevEntry':ciscoScsiTgtDevEntry,_AE:ciscoScsiTgtDevNumberOfLUs,_U:ciscoScsiTgtDeviceStatus,_AF:ciscoScsiTgtDevNonAccLUs,'ciscoScsiTgtPortTable':ciscoScsiTgtPortTable,'ciscoScsiTgtPortEntry':ciscoScsiTgtPortEntry,_AG:ciscoScsiTgtPortName,_AH:ciscoScsiTgtPortIdentifier,_Ad:ciscoScsiTgtPortInCommands,_Ae:ciscoScsiTgtPortWrMegaBytes,_Af:ciscoScsiTgtPortReadMegaBytes,_Al:ciscoScsiTgtPortHSInCommands,'ciscoScsiRemoteInitiators':ciscoScsiRemoteInitiators,'ciscoScsiAuthorizedIntrTable':ciscoScsiAuthorizedIntrTable,'ciscoScsiAuthorizedIntrEntry':ciscoScsiAuthorizedIntrEntry,_f:ciscoScsiAuthIntrTgtPortIndex,_g:ciscoScsiAuthIntrIndex,_AY:ciscoScsiAuthIntrDevOrPort,_AZ:ciscoScsiAuthIntrName,_Aa:ciscoScsiAuthIntrLunMapIndex,_An:ciscoScsiAuthIntrAttachedTimes,_Ao:ciscoScsiAuthIntrOutCommands,_Ap:ciscoScsiAuthIntrReadMegaBytes,_Aq:ciscoScsiAuthIntrWrMegaBytes,_Ar:ciscoScsiAuthIntrHSOutCommands,_Ab:ciscoScsiAuthIntrLastCreation,_Ac:ciscoScsiAuthIntrRowStatus,'ciscoScsiAttIntrPrtTable':ciscoScsiAttIntrPrtTable,'ciscoScsiAttIntrPrtEntry':ciscoScsiAttIntrPrtEntry,_h:ciscoScsiAttIntrPrtIdx,_AI:ciscoScsiAttIntrPrtAuthIntrIdx,_AJ:ciscoScsiAttIntrPrtName,_AK:ciscoScsiAttIntrPrtId,'ciscoScsiLogicalUnit':ciscoScsiLogicalUnit,'ciscoScsiLuTable':ciscoScsiLuTable,'ciscoScsiLuEntry':ciscoScsiLuEntry,_T:ciscoScsiLuIndex,_AL:ciscoScsiLuDefaultLun,_AM:ciscoScsiLuWwnName,_AN:ciscoScsiLuVendorId,_AO:ciscoScsiLuProductId,_AP:ciscoScsiLuRevisionId,_AQ:ciscoScsiLuPeripheralType,_V:ciscoScsiLuStatus,_AR:ciscoScsiLuState,_Ag:ciscoScsiLuInCommands,_Ah:ciscoScsiLuReadMegaBytes,_Ai:ciscoScsiLuWrittenMegaBytes,_Aj:ciscoScsiLuInResets,_Ak:ciscoScsiLuOutQueueFullStatus,_Am:ciscoScsiLuHSInCommands,'ciscoScsiLuIdTable':ciscoScsiLuIdTable,'ciscoScsiLuIdEntry':ciscoScsiLuIdEntry,_i:ciscoScsiLuIdIndex,_AS:ciscoScsiLuIdCodeSet,_AT:ciscoScsiLuIdAssociation,_AU:ciscoScsiLuIdType,_AV:ciscoScsiLuIdValue,'ciscoScsiLunMapTable':ciscoScsiLunMapTable,'ciscoScsiLunMapEntry':ciscoScsiLunMapEntry,_j:ciscoScsiLunMapIndex,_k:ciscoScsiLunMapLun,_AW:ciscoScsiLunMapLuIndex,_AX:ciscoScsiLunMapRowStatus,'ciscoScsiNotification':ciscoScsiNotification,'ciscoScsiNotifications':ciscoScsiNotifications,_B2:ciscoScsiTgtDevStatusChanged,_B3:ciscoScsiLuStatusChanged,'ciscoScsiConformance':ciscoScsiConformance,'ciscoScsiCompliances':ciscoScsiCompliances,'ciscoScsiCompliance':ciscoScsiCompliance,'ciscoScsiGroups':ciscoScsiGroups,_B4:ciscoScsiDeviceGroup,'ciscoScsiInitiatorGroup':ciscoScsiInitiatorGroup,'ciscoScsiDiscoveryGroup':ciscoScsiDiscoveryGroup,'ciscoScsiTargetGroup':ciscoScsiTargetGroup,'ciscoScsiLunMapGroup':ciscoScsiLunMapGroup,'ciscoScsiTargetStatsGroup':ciscoScsiTargetStatsGroup,'ciscoScsiTargetHSStatsGroup':ciscoScsiTargetHSStatsGroup,'ciscoScsiLunMapStatsGroup':ciscoScsiLunMapStatsGroup,'ciscoScsiLunMapHSStatsGroup':ciscoScsiLunMapHSStatsGroup,'ciscoScsiInitiatorStatsGroup':ciscoScsiInitiatorStatsGroup,'ciscoScsiInitiatorHSStatsGroup':ciscoScsiInitiatorHSStatsGroup,'ciscoScsiDiscoveryStatsGroup':ciscoScsiDiscoveryStatsGroup,'ciscoScsiDiscoveryHSStatsGroup':ciscoScsiDiscoveryHSStatsGroup,'ciscoScsiDeviceStatGroup':ciscoScsiDeviceStatGroup,'ciscoScsiNotifGroup':ciscoScsiNotifGroup})