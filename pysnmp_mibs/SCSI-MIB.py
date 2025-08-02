_B3='scsiDeviceGroup'
_B2='scsiPortBusyStatuses'
_B1='scsiDeviceResets'
_B0='scsiDscTgtHSInCommands'
_A_='scsiDscTgtWrittenMegaBytes'
_Az='scsiDscTgtReadMegaBytes'
_Ay='scsiDscTgtInCommands'
_Ax='scsiIntrPrtHSOutCommands'
_Aw='scsiIntrPrtReadMegaBytes'
_Av='scsiIntrPrtWrittenMegaBytes'
_Au='scsiIntrPrtOutCommands'
_At='scsiIntrDevOutResets'
_As='scsiAuthIntrHSOutCommands'
_Ar='scsiAuthIntrWrittenMegaBytes'
_Aq='scsiAuthIntrReadMegaBytes'
_Ap='scsiAuthIntrOutCommands'
_Ao='scsiAuthIntrAttachedTimes'
_An='scsiLuHSInCommands'
_Am='scsiTgtPortHSInCommands'
_Al='scsiLuOutQueueFullStatus'
_Ak='scsiLuInResets'
_Aj='scsiLuWrittenMegaBytes'
_Ai='scsiLuReadMegaBytes'
_Ah='scsiLuInCommands'
_Ag='scsiTgtPortReadMegaBytes'
_Af='scsiTgtPortWrittenMegaBytes'
_Ae='scsiTgtPortInCommands'
_Ad='scsiAuthIntrRowStatus'
_Ac='scsiAuthIntrLastCreation'
_Ab='scsiAuthIntrLunMapIndex'
_Aa='scsiAuthIntrName'
_AZ='scsiAuthIntrDevOrPort'
_AY='scsiLunMapRowStatus'
_AX='scsiLunMapLuIndex'
_AW='scsiLuIdValue'
_AV='scsiLuIdType'
_AU='scsiLuIdAssociation'
_AT='scsiLuIdCodeSet'
_AS='scsiLuState'
_AR='scsiLuPeripheralType'
_AQ='scsiLuRevisionId'
_AP='scsiLuProductId'
_AO='scsiLuVendorId'
_AN='scsiLuWwnName'
_AM='scsiLuDefaultLun'
_AL='scsiAttIntrPrtId'
_AK='scsiAttIntrPrtName'
_AJ='scsiAttIntrPrtAuthIntrIdx'
_AI='scsiTgtPortIdentifier'
_AH='scsiTgtPortName'
_AG='scsiTgtDevNonAccessibleLUs'
_AF='scsiTgtDevNumberOfLUs'
_AE='scsiDscLunIdValue'
_AD='scsiDscLunIdType'
_AC='scsiDscLunIdAssociation'
_AB='scsiDscLunIdCodeSet'
_AA='scsiDscLunLun'
_A9='scsiDscTgtLastCreation'
_A8='scsiDscTgtRowStatus'
_A7='scsiDscTgtDiscovered'
_A6='scsiDscTgtConfigured'
_A5='scsiDscTgtName'
_A4='scsiDscTgtDevOrPort'
_A3='scsiAttTgtPortIdentifier'
_A2='scsiAttTgtPortName'
_A1='scsiAttTgtPortDscTgtIdx'
_A0='scsiIntrPrtIdentifier'
_z='scsiIntrPrtName'
_y='scsiIntrDevTgtAccessMode'
_x='scsiTrnsptDevName'
_w='scsiTrnsptPointer'
_v='scsiTrnsptType'
_u='scsiPortTrnsptPtr'
_t='scsiPortRole'
_s='scsiDevicePortNumber'
_r='scsiDeviceRole'
_q='scsiDeviceAlias'
_p='scsiInstScsiNotificationsEnable'
_o='scsiInstVendorVersion'
_n='scsiInstSoftwareIndex'
_m='scsiInstAlias'
_l='scsiLunMapLun'
_k='scsiLunMapIndex'
_j='scsiLuIdIndex'
_i='scsiAttIntrPrtIdx'
_h='scsiAuthIntrIndex'
_g='scsiAuthIntrTgtPortIndex'
_f='abnormal'
_e='readying'
_d='broken'
_c='available'
_b='scsiAttTgtPortIndex'
_a='scsiDscLunIdIndex'
_Z='scsiTrnsptIndex'
_Y='initiator'
_X='target'
_W='scsiLuStatus'
_V='scsiTgtDeviceStatus'
_U='scsiLuIndex'
_T='scsiDscLunIndex'
_S='unknown'
_R='TruthValue'
_Q='scsiDscTgtIndex'
_P='scsiDscTgtIntrPortIndex'
_O='read-write'
_N='Integer32'
_M='Bits'
_L='OctetString'
_K='scsiPortIndex'
_J='SnmpAdminString'
_I='read-create'
_H='Megabytes'
_G='commands'
_F='not-accessible'
_E='scsiDeviceIndex'
_D='scsiInstIndex'
_C='read-only'
_B='SCSI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI',_M,'Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
AutonomousType,DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp',_R)
scsiModule=ModuleIdentity((1,3,6,1,2,1,999))
if mibBuilder.loadTexts:scsiModule.setRevisions(('2002-02-25 00:00',))
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
_ScsiObjects_ObjectIdentity=ObjectIdentity
scsiObjects=_ScsiObjects_ObjectIdentity((1,3,6,1,2,1,999,1))
_ScsiTransportTypes_ObjectIdentity=ObjectIdentity
scsiTransportTypes=_ScsiTransportTypes_ObjectIdentity((1,3,6,1,2,1,999,1,1))
_ScsiTranportOther_ObjectIdentity=ObjectIdentity
scsiTranportOther=_ScsiTranportOther_ObjectIdentity((1,3,6,1,2,1,999,1,1,1))
_ScsiTranportSPI_ObjectIdentity=ObjectIdentity
scsiTranportSPI=_ScsiTranportSPI_ObjectIdentity((1,3,6,1,2,1,999,1,1,2))
_ScsiTransportFCP_ObjectIdentity=ObjectIdentity
scsiTransportFCP=_ScsiTransportFCP_ObjectIdentity((1,3,6,1,2,1,999,1,1,3))
_ScsiTransportSRP_ObjectIdentity=ObjectIdentity
scsiTransportSRP=_ScsiTransportSRP_ObjectIdentity((1,3,6,1,2,1,999,1,1,4))
_ScsiTransportISCSI_ObjectIdentity=ObjectIdentity
scsiTransportISCSI=_ScsiTransportISCSI_ObjectIdentity((1,3,6,1,2,1,999,1,1,5))
_ScsiTransportSBP_ObjectIdentity=ObjectIdentity
scsiTransportSBP=_ScsiTransportSBP_ObjectIdentity((1,3,6,1,2,1,999,1,1,6))
_ScsiGeneral_ObjectIdentity=ObjectIdentity
scsiGeneral=_ScsiGeneral_ObjectIdentity((1,3,6,1,2,1,999,1,2))
_ScsiInstanceTable_Object=MibTable
scsiInstanceTable=_ScsiInstanceTable_Object((1,3,6,1,2,1,999,1,2,1))
if mibBuilder.loadTexts:scsiInstanceTable.setStatus(_A)
_ScsiInstanceEntry_Object=MibTableRow
scsiInstanceEntry=_ScsiInstanceEntry_Object((1,3,6,1,2,1,999,1,2,1,1))
scsiInstanceEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:scsiInstanceEntry.setStatus(_A)
_ScsiInstIndex_Type=ScsiIndexValue
_ScsiInstIndex_Object=MibTableColumn
scsiInstIndex=_ScsiInstIndex_Object((1,3,6,1,2,1,999,1,2,1,1,1),_ScsiInstIndex_Type())
scsiInstIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiInstIndex.setStatus(_A)
class _ScsiInstAlias_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ScsiInstAlias_Type.__name__=_J
_ScsiInstAlias_Object=MibTableColumn
scsiInstAlias=_ScsiInstAlias_Object((1,3,6,1,2,1,999,1,2,1,1,2),_ScsiInstAlias_Type())
scsiInstAlias.setMaxAccess(_O)
if mibBuilder.loadTexts:scsiInstAlias.setStatus(_A)
_ScsiInstSoftwareIndex_Type=HrSWInstalledIndexOrZero
_ScsiInstSoftwareIndex_Object=MibTableColumn
scsiInstSoftwareIndex=_ScsiInstSoftwareIndex_Object((1,3,6,1,2,1,999,1,2,1,1,3),_ScsiInstSoftwareIndex_Type())
scsiInstSoftwareIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiInstSoftwareIndex.setStatus(_A)
class _ScsiInstVendorVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ScsiInstVendorVersion_Type.__name__=_J
_ScsiInstVendorVersion_Object=MibTableColumn
scsiInstVendorVersion=_ScsiInstVendorVersion_Object((1,3,6,1,2,1,999,1,2,1,1,4),_ScsiInstVendorVersion_Type())
scsiInstVendorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiInstVendorVersion.setStatus(_A)
class _ScsiInstScsiNotificationsEnable_Type(TruthValue):defaultValue=1
_ScsiInstScsiNotificationsEnable_Type.__name__=_R
_ScsiInstScsiNotificationsEnable_Object=MibTableColumn
scsiInstScsiNotificationsEnable=_ScsiInstScsiNotificationsEnable_Object((1,3,6,1,2,1,999,1,2,1,1,5),_ScsiInstScsiNotificationsEnable_Type())
scsiInstScsiNotificationsEnable.setMaxAccess(_O)
if mibBuilder.loadTexts:scsiInstScsiNotificationsEnable.setStatus(_A)
_ScsiDeviceTable_Object=MibTable
scsiDeviceTable=_ScsiDeviceTable_Object((1,3,6,1,2,1,999,1,2,2))
if mibBuilder.loadTexts:scsiDeviceTable.setStatus(_A)
_ScsiDeviceEntry_Object=MibTableRow
scsiDeviceEntry=_ScsiDeviceEntry_Object((1,3,6,1,2,1,999,1,2,2,1))
scsiDeviceEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:scsiDeviceEntry.setStatus(_A)
_ScsiDeviceIndex_Type=ScsiIndexValue
_ScsiDeviceIndex_Object=MibTableColumn
scsiDeviceIndex=_ScsiDeviceIndex_Object((1,3,6,1,2,1,999,1,2,2,1,1),_ScsiDeviceIndex_Type())
scsiDeviceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiDeviceIndex.setStatus(_A)
class _ScsiDeviceAlias_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ScsiDeviceAlias_Type.__name__=_J
_ScsiDeviceAlias_Object=MibTableColumn
scsiDeviceAlias=_ScsiDeviceAlias_Object((1,3,6,1,2,1,999,1,2,2,1,2),_ScsiDeviceAlias_Type())
scsiDeviceAlias.setMaxAccess(_O)
if mibBuilder.loadTexts:scsiDeviceAlias.setStatus(_A)
class _ScsiDeviceRole_Type(Bits):namedValues=NamedValues(*((_X,0),(_Y,1)))
_ScsiDeviceRole_Type.__name__=_M
_ScsiDeviceRole_Object=MibTableColumn
scsiDeviceRole=_ScsiDeviceRole_Object((1,3,6,1,2,1,999,1,2,2,1,3),_ScsiDeviceRole_Type())
scsiDeviceRole.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDeviceRole.setStatus(_A)
_ScsiDevicePortNumber_Type=Unsigned32
_ScsiDevicePortNumber_Object=MibTableColumn
scsiDevicePortNumber=_ScsiDevicePortNumber_Object((1,3,6,1,2,1,999,1,2,2,1,4),_ScsiDevicePortNumber_Type())
scsiDevicePortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDevicePortNumber.setStatus(_A)
_ScsiDeviceResets_Type=Counter32
_ScsiDeviceResets_Object=MibTableColumn
scsiDeviceResets=_ScsiDeviceResets_Object((1,3,6,1,2,1,999,1,2,2,1,5),_ScsiDeviceResets_Type())
scsiDeviceResets.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDeviceResets.setStatus(_A)
_ScsiPortTable_Object=MibTable
scsiPortTable=_ScsiPortTable_Object((1,3,6,1,2,1,999,1,2,3))
if mibBuilder.loadTexts:scsiPortTable.setStatus(_A)
_ScsiPortEntry_Object=MibTableRow
scsiPortEntry=_ScsiPortEntry_Object((1,3,6,1,2,1,999,1,2,3,1))
scsiPortEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_K))
if mibBuilder.loadTexts:scsiPortEntry.setStatus(_A)
_ScsiPortIndex_Type=ScsiIndexValue
_ScsiPortIndex_Object=MibTableColumn
scsiPortIndex=_ScsiPortIndex_Object((1,3,6,1,2,1,999,1,2,3,1,1),_ScsiPortIndex_Type())
scsiPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiPortIndex.setStatus(_A)
class _ScsiPortRole_Type(Bits):namedValues=NamedValues(*((_X,0),(_Y,1)))
_ScsiPortRole_Type.__name__=_M
_ScsiPortRole_Object=MibTableColumn
scsiPortRole=_ScsiPortRole_Object((1,3,6,1,2,1,999,1,2,3,1,2),_ScsiPortRole_Type())
scsiPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiPortRole.setStatus(_A)
class _ScsiPortTrnsptPtr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ScsiPortTrnsptPtr_Type.__name__=_L
_ScsiPortTrnsptPtr_Object=MibTableColumn
scsiPortTrnsptPtr=_ScsiPortTrnsptPtr_Object((1,3,6,1,2,1,999,1,2,3,1,3),_ScsiPortTrnsptPtr_Type())
scsiPortTrnsptPtr.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiPortTrnsptPtr.setStatus(_A)
_ScsiPortBusyStatuses_Type=Counter32
_ScsiPortBusyStatuses_Object=MibTableColumn
scsiPortBusyStatuses=_ScsiPortBusyStatuses_Object((1,3,6,1,2,1,999,1,2,3,1,4),_ScsiPortBusyStatuses_Type())
scsiPortBusyStatuses.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiPortBusyStatuses.setStatus(_A)
_ScsiTrnsptTable_Object=MibTable
scsiTrnsptTable=_ScsiTrnsptTable_Object((1,3,6,1,2,1,999,1,2,5))
if mibBuilder.loadTexts:scsiTrnsptTable.setStatus(_A)
_ScsiTrnsptEntry_Object=MibTableRow
scsiTrnsptEntry=_ScsiTrnsptEntry_Object((1,3,6,1,2,1,999,1,2,5,1))
scsiTrnsptEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_Z))
if mibBuilder.loadTexts:scsiTrnsptEntry.setStatus(_A)
_ScsiTrnsptIndex_Type=ScsiIndexValue
_ScsiTrnsptIndex_Object=MibTableColumn
scsiTrnsptIndex=_ScsiTrnsptIndex_Object((1,3,6,1,2,1,999,1,2,5,1,1),_ScsiTrnsptIndex_Type())
scsiTrnsptIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiTrnsptIndex.setStatus(_A)
class _ScsiTrnsptType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ScsiTrnsptType_Type.__name__=_L
_ScsiTrnsptType_Object=MibTableColumn
scsiTrnsptType=_ScsiTrnsptType_Object((1,3,6,1,2,1,999,1,2,5,1,2),_ScsiTrnsptType_Type())
scsiTrnsptType.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiTrnsptType.setStatus(_A)
class _ScsiTrnsptPointer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_ScsiTrnsptPointer_Type.__name__=_L
_ScsiTrnsptPointer_Object=MibTableColumn
scsiTrnsptPointer=_ScsiTrnsptPointer_Object((1,3,6,1,2,1,999,1,2,5,1,3),_ScsiTrnsptPointer_Type())
scsiTrnsptPointer.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiTrnsptPointer.setStatus(_A)
_ScsiTrnsptDevName_Type=ScsiName
_ScsiTrnsptDevName_Object=MibTableColumn
scsiTrnsptDevName=_ScsiTrnsptDevName_Object((1,3,6,1,2,1,999,1,2,5,1,4),_ScsiTrnsptDevName_Type())
scsiTrnsptDevName.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiTrnsptDevName.setStatus(_A)
_ScsiInitiator_ObjectIdentity=ObjectIdentity
scsiInitiator=_ScsiInitiator_ObjectIdentity((1,3,6,1,2,1,999,1,3))
_ScsiIntrDevTable_Object=MibTable
scsiIntrDevTable=_ScsiIntrDevTable_Object((1,3,6,1,2,1,999,1,3,1))
if mibBuilder.loadTexts:scsiIntrDevTable.setStatus(_A)
_ScsiIntrDevEntry_Object=MibTableRow
scsiIntrDevEntry=_ScsiIntrDevEntry_Object((1,3,6,1,2,1,999,1,3,1,1))
scsiIntrDevEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:scsiIntrDevEntry.setStatus(_A)
class _ScsiIntrDevTgtAccessMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('autoEnable',2),('manualEnable',3)))
_ScsiIntrDevTgtAccessMode_Type.__name__=_N
_ScsiIntrDevTgtAccessMode_Object=MibTableColumn
scsiIntrDevTgtAccessMode=_ScsiIntrDevTgtAccessMode_Object((1,3,6,1,2,1,999,1,3,1,1,1),_ScsiIntrDevTgtAccessMode_Type())
scsiIntrDevTgtAccessMode.setMaxAccess(_O)
if mibBuilder.loadTexts:scsiIntrDevTgtAccessMode.setStatus(_A)
_ScsiIntrDevOutResets_Type=Counter32
_ScsiIntrDevOutResets_Object=MibTableColumn
scsiIntrDevOutResets=_ScsiIntrDevOutResets_Object((1,3,6,1,2,1,999,1,3,1,1,2),_ScsiIntrDevOutResets_Type())
scsiIntrDevOutResets.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiIntrDevOutResets.setStatus(_A)
_ScsiIntrPrtTable_Object=MibTable
scsiIntrPrtTable=_ScsiIntrPrtTable_Object((1,3,6,1,2,1,999,1,3,3))
if mibBuilder.loadTexts:scsiIntrPrtTable.setStatus(_A)
_ScsiIntrPrtEntry_Object=MibTableRow
scsiIntrPrtEntry=_ScsiIntrPrtEntry_Object((1,3,6,1,2,1,999,1,3,3,1))
scsiIntrPrtEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_K))
if mibBuilder.loadTexts:scsiIntrPrtEntry.setStatus(_A)
_ScsiIntrPrtName_Type=ScsiName
_ScsiIntrPrtName_Object=MibTableColumn
scsiIntrPrtName=_ScsiIntrPrtName_Object((1,3,6,1,2,1,999,1,3,3,1,1),_ScsiIntrPrtName_Type())
scsiIntrPrtName.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiIntrPrtName.setStatus(_A)
_ScsiIntrPrtIdentifier_Type=ScsiIdentifier
_ScsiIntrPrtIdentifier_Object=MibTableColumn
scsiIntrPrtIdentifier=_ScsiIntrPrtIdentifier_Object((1,3,6,1,2,1,999,1,3,3,1,2),_ScsiIntrPrtIdentifier_Type())
scsiIntrPrtIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiIntrPrtIdentifier.setStatus(_A)
_ScsiIntrPrtOutCommands_Type=Counter32
_ScsiIntrPrtOutCommands_Object=MibTableColumn
scsiIntrPrtOutCommands=_ScsiIntrPrtOutCommands_Object((1,3,6,1,2,1,999,1,3,3,1,3),_ScsiIntrPrtOutCommands_Type())
scsiIntrPrtOutCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiIntrPrtOutCommands.setStatus(_A)
if mibBuilder.loadTexts:scsiIntrPrtOutCommands.setUnits(_G)
_ScsiIntrPrtWrittenMegaBytes_Type=Counter32
_ScsiIntrPrtWrittenMegaBytes_Object=MibTableColumn
scsiIntrPrtWrittenMegaBytes=_ScsiIntrPrtWrittenMegaBytes_Object((1,3,6,1,2,1,999,1,3,3,1,4),_ScsiIntrPrtWrittenMegaBytes_Type())
scsiIntrPrtWrittenMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiIntrPrtWrittenMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:scsiIntrPrtWrittenMegaBytes.setUnits(_H)
_ScsiIntrPrtReadMegaBytes_Type=Counter32
_ScsiIntrPrtReadMegaBytes_Object=MibTableColumn
scsiIntrPrtReadMegaBytes=_ScsiIntrPrtReadMegaBytes_Object((1,3,6,1,2,1,999,1,3,3,1,5),_ScsiIntrPrtReadMegaBytes_Type())
scsiIntrPrtReadMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiIntrPrtReadMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:scsiIntrPrtReadMegaBytes.setUnits(_H)
_ScsiIntrPrtHSOutCommands_Type=Counter64
_ScsiIntrPrtHSOutCommands_Object=MibTableColumn
scsiIntrPrtHSOutCommands=_ScsiIntrPrtHSOutCommands_Object((1,3,6,1,2,1,999,1,3,3,1,6),_ScsiIntrPrtHSOutCommands_Type())
scsiIntrPrtHSOutCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiIntrPrtHSOutCommands.setStatus(_A)
if mibBuilder.loadTexts:scsiIntrPrtHSOutCommands.setUnits(_G)
_ScsiRemoteTarget_ObjectIdentity=ObjectIdentity
scsiRemoteTarget=_ScsiRemoteTarget_ObjectIdentity((1,3,6,1,2,1,999,1,3,4))
_ScsiDscTgtTable_Object=MibTable
scsiDscTgtTable=_ScsiDscTgtTable_Object((1,3,6,1,2,1,999,1,3,4,1))
if mibBuilder.loadTexts:scsiDscTgtTable.setStatus(_A)
_ScsiDscTgtEntry_Object=MibTableRow
scsiDscTgtEntry=_ScsiDscTgtEntry_Object((1,3,6,1,2,1,999,1,3,4,1,1))
scsiDscTgtEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:scsiDscTgtEntry.setStatus(_A)
_ScsiDscTgtIntrPortIndex_Type=ScsiPortIndexValueOrZero
_ScsiDscTgtIntrPortIndex_Object=MibTableColumn
scsiDscTgtIntrPortIndex=_ScsiDscTgtIntrPortIndex_Object((1,3,6,1,2,1,999,1,3,4,1,1,1),_ScsiDscTgtIntrPortIndex_Type())
scsiDscTgtIntrPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiDscTgtIntrPortIndex.setStatus(_A)
_ScsiDscTgtIndex_Type=ScsiIndexValue
_ScsiDscTgtIndex_Object=MibTableColumn
scsiDscTgtIndex=_ScsiDscTgtIndex_Object((1,3,6,1,2,1,999,1,3,4,1,1,2),_ScsiDscTgtIndex_Type())
scsiDscTgtIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiDscTgtIndex.setStatus(_A)
_ScsiDscTgtDevOrPort_Type=ScsiDeviceOrPort
_ScsiDscTgtDevOrPort_Object=MibTableColumn
scsiDscTgtDevOrPort=_ScsiDscTgtDevOrPort_Object((1,3,6,1,2,1,999,1,3,4,1,1,3),_ScsiDscTgtDevOrPort_Type())
scsiDscTgtDevOrPort.setMaxAccess(_I)
if mibBuilder.loadTexts:scsiDscTgtDevOrPort.setStatus(_A)
_ScsiDscTgtName_Type=ScsiName
_ScsiDscTgtName_Object=MibTableColumn
scsiDscTgtName=_ScsiDscTgtName_Object((1,3,6,1,2,1,999,1,3,4,1,1,4),_ScsiDscTgtName_Type())
scsiDscTgtName.setMaxAccess(_I)
if mibBuilder.loadTexts:scsiDscTgtName.setStatus(_A)
class _ScsiDscTgtConfigured_Type(TruthValue):defaultValue=1
_ScsiDscTgtConfigured_Type.__name__=_R
_ScsiDscTgtConfigured_Object=MibTableColumn
scsiDscTgtConfigured=_ScsiDscTgtConfigured_Object((1,3,6,1,2,1,999,1,3,4,1,1,5),_ScsiDscTgtConfigured_Type())
scsiDscTgtConfigured.setMaxAccess(_I)
if mibBuilder.loadTexts:scsiDscTgtConfigured.setStatus(_A)
_ScsiDscTgtDiscovered_Type=TruthValue
_ScsiDscTgtDiscovered_Object=MibTableColumn
scsiDscTgtDiscovered=_ScsiDscTgtDiscovered_Object((1,3,6,1,2,1,999,1,3,4,1,1,6),_ScsiDscTgtDiscovered_Type())
scsiDscTgtDiscovered.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDscTgtDiscovered.setStatus(_A)
_ScsiDscTgtInCommands_Type=Counter32
_ScsiDscTgtInCommands_Object=MibTableColumn
scsiDscTgtInCommands=_ScsiDscTgtInCommands_Object((1,3,6,1,2,1,999,1,3,4,1,1,7),_ScsiDscTgtInCommands_Type())
scsiDscTgtInCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDscTgtInCommands.setStatus(_A)
if mibBuilder.loadTexts:scsiDscTgtInCommands.setUnits(_G)
_ScsiDscTgtWrittenMegaBytes_Type=Counter32
_ScsiDscTgtWrittenMegaBytes_Object=MibTableColumn
scsiDscTgtWrittenMegaBytes=_ScsiDscTgtWrittenMegaBytes_Object((1,3,6,1,2,1,999,1,3,4,1,1,8),_ScsiDscTgtWrittenMegaBytes_Type())
scsiDscTgtWrittenMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDscTgtWrittenMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:scsiDscTgtWrittenMegaBytes.setUnits(_H)
_ScsiDscTgtReadMegaBytes_Type=Counter32
_ScsiDscTgtReadMegaBytes_Object=MibTableColumn
scsiDscTgtReadMegaBytes=_ScsiDscTgtReadMegaBytes_Object((1,3,6,1,2,1,999,1,3,4,1,1,9),_ScsiDscTgtReadMegaBytes_Type())
scsiDscTgtReadMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDscTgtReadMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:scsiDscTgtReadMegaBytes.setUnits(_H)
_ScsiDscTgtHSInCommands_Type=Counter64
_ScsiDscTgtHSInCommands_Object=MibTableColumn
scsiDscTgtHSInCommands=_ScsiDscTgtHSInCommands_Object((1,3,6,1,2,1,999,1,3,4,1,1,10),_ScsiDscTgtHSInCommands_Type())
scsiDscTgtHSInCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDscTgtHSInCommands.setStatus(_A)
if mibBuilder.loadTexts:scsiDscTgtHSInCommands.setUnits(_G)
_ScsiDscTgtLastCreation_Type=TimeStamp
_ScsiDscTgtLastCreation_Object=MibTableColumn
scsiDscTgtLastCreation=_ScsiDscTgtLastCreation_Object((1,3,6,1,2,1,999,1,3,4,1,1,11),_ScsiDscTgtLastCreation_Type())
scsiDscTgtLastCreation.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDscTgtLastCreation.setStatus(_A)
_ScsiDscTgtRowStatus_Type=RowStatus
_ScsiDscTgtRowStatus_Object=MibTableColumn
scsiDscTgtRowStatus=_ScsiDscTgtRowStatus_Object((1,3,6,1,2,1,999,1,3,4,1,1,12),_ScsiDscTgtRowStatus_Type())
scsiDscTgtRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:scsiDscTgtRowStatus.setStatus(_A)
_ScsiDscLunTable_Object=MibTable
scsiDscLunTable=_ScsiDscLunTable_Object((1,3,6,1,2,1,999,1,3,4,2))
if mibBuilder.loadTexts:scsiDscLunTable.setStatus(_A)
_ScsiDscLunEntry_Object=MibTableRow
scsiDscLunEntry=_ScsiDscLunEntry_Object((1,3,6,1,2,1,999,1,3,4,2,1))
scsiDscLunEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_P),(0,_B,_Q),(0,_B,_T))
if mibBuilder.loadTexts:scsiDscLunEntry.setStatus(_A)
_ScsiDscLunIndex_Type=ScsiIndexValue
_ScsiDscLunIndex_Object=MibTableColumn
scsiDscLunIndex=_ScsiDscLunIndex_Object((1,3,6,1,2,1,999,1,3,4,2,1,1),_ScsiDscLunIndex_Type())
scsiDscLunIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiDscLunIndex.setStatus(_A)
_ScsiDscLunLun_Type=ScsiLUNOrZero
_ScsiDscLunLun_Object=MibTableColumn
scsiDscLunLun=_ScsiDscLunLun_Object((1,3,6,1,2,1,999,1,3,4,2,1,2),_ScsiDscLunLun_Type())
scsiDscLunLun.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDscLunLun.setStatus(_A)
_ScsiDscLunIdTable_Object=MibTable
scsiDscLunIdTable=_ScsiDscLunIdTable_Object((1,3,6,1,2,1,999,1,3,4,3))
if mibBuilder.loadTexts:scsiDscLunIdTable.setStatus(_A)
_ScsiDscLunIdEntry_Object=MibTableRow
scsiDscLunIdEntry=_ScsiDscLunIdEntry_Object((1,3,6,1,2,1,999,1,3,4,3,1))
scsiDscLunIdEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_P),(0,_B,_Q),(0,_B,_T),(0,_B,_a))
if mibBuilder.loadTexts:scsiDscLunIdEntry.setStatus(_A)
_ScsiDscLunIdIndex_Type=ScsiIndexValue
_ScsiDscLunIdIndex_Object=MibTableColumn
scsiDscLunIdIndex=_ScsiDscLunIdIndex_Object((1,3,6,1,2,1,999,1,3,4,3,1,1),_ScsiDscLunIdIndex_Type())
scsiDscLunIdIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiDscLunIdIndex.setStatus(_A)
_ScsiDscLunIdCodeSet_Type=ScsiIdCodeSet
_ScsiDscLunIdCodeSet_Object=MibTableColumn
scsiDscLunIdCodeSet=_ScsiDscLunIdCodeSet_Object((1,3,6,1,2,1,999,1,3,4,3,1,2),_ScsiDscLunIdCodeSet_Type())
scsiDscLunIdCodeSet.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDscLunIdCodeSet.setStatus(_A)
_ScsiDscLunIdAssociation_Type=ScsiIdAssociation
_ScsiDscLunIdAssociation_Object=MibTableColumn
scsiDscLunIdAssociation=_ScsiDscLunIdAssociation_Object((1,3,6,1,2,1,999,1,3,4,3,1,3),_ScsiDscLunIdAssociation_Type())
scsiDscLunIdAssociation.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDscLunIdAssociation.setStatus(_A)
_ScsiDscLunIdType_Type=ScsiIdType
_ScsiDscLunIdType_Object=MibTableColumn
scsiDscLunIdType=_ScsiDscLunIdType_Object((1,3,6,1,2,1,999,1,3,4,3,1,4),_ScsiDscLunIdType_Type())
scsiDscLunIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDscLunIdType.setStatus(_A)
_ScsiDscLunIdValue_Type=ScsiIdValue
_ScsiDscLunIdValue_Object=MibTableColumn
scsiDscLunIdValue=_ScsiDscLunIdValue_Object((1,3,6,1,2,1,999,1,3,4,3,1,5),_ScsiDscLunIdValue_Type())
scsiDscLunIdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiDscLunIdValue.setStatus(_A)
_ScsiAttTgtPortTable_Object=MibTable
scsiAttTgtPortTable=_ScsiAttTgtPortTable_Object((1,3,6,1,2,1,999,1,3,4,6))
if mibBuilder.loadTexts:scsiAttTgtPortTable.setStatus(_A)
_ScsiAttTgtPortEntry_Object=MibTableRow
scsiAttTgtPortEntry=_ScsiAttTgtPortEntry_Object((1,3,6,1,2,1,999,1,3,4,6,1))
scsiAttTgtPortEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_K),(0,_B,_b))
if mibBuilder.loadTexts:scsiAttTgtPortEntry.setStatus(_A)
_ScsiAttTgtPortIndex_Type=ScsiIndexValue
_ScsiAttTgtPortIndex_Object=MibTableColumn
scsiAttTgtPortIndex=_ScsiAttTgtPortIndex_Object((1,3,6,1,2,1,999,1,3,4,6,1,1),_ScsiAttTgtPortIndex_Type())
scsiAttTgtPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiAttTgtPortIndex.setStatus(_A)
_ScsiAttTgtPortDscTgtIdx_Type=ScsiIndexValueOrZero
_ScsiAttTgtPortDscTgtIdx_Object=MibTableColumn
scsiAttTgtPortDscTgtIdx=_ScsiAttTgtPortDscTgtIdx_Object((1,3,6,1,2,1,999,1,3,4,6,1,2),_ScsiAttTgtPortDscTgtIdx_Type())
scsiAttTgtPortDscTgtIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiAttTgtPortDscTgtIdx.setStatus(_A)
_ScsiAttTgtPortName_Type=ScsiName
_ScsiAttTgtPortName_Object=MibTableColumn
scsiAttTgtPortName=_ScsiAttTgtPortName_Object((1,3,6,1,2,1,999,1,3,4,6,1,3),_ScsiAttTgtPortName_Type())
scsiAttTgtPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiAttTgtPortName.setStatus(_A)
_ScsiAttTgtPortIdentifier_Type=ScsiIdentifier
_ScsiAttTgtPortIdentifier_Object=MibTableColumn
scsiAttTgtPortIdentifier=_ScsiAttTgtPortIdentifier_Object((1,3,6,1,2,1,999,1,3,4,6,1,4),_ScsiAttTgtPortIdentifier_Type())
scsiAttTgtPortIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiAttTgtPortIdentifier.setStatus(_A)
_ScsiTarget_ObjectIdentity=ObjectIdentity
scsiTarget=_ScsiTarget_ObjectIdentity((1,3,6,1,2,1,999,1,4))
_ScsiTgtDevTable_Object=MibTable
scsiTgtDevTable=_ScsiTgtDevTable_Object((1,3,6,1,2,1,999,1,4,1))
if mibBuilder.loadTexts:scsiTgtDevTable.setStatus(_A)
_ScsiTgtDevEntry_Object=MibTableRow
scsiTgtDevEntry=_ScsiTgtDevEntry_Object((1,3,6,1,2,1,999,1,4,1,1))
scsiTgtDevEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:scsiTgtDevEntry.setStatus(_A)
_ScsiTgtDevNumberOfLUs_Type=Gauge32
_ScsiTgtDevNumberOfLUs_Object=MibTableColumn
scsiTgtDevNumberOfLUs=_ScsiTgtDevNumberOfLUs_Object((1,3,6,1,2,1,999,1,4,1,1,1),_ScsiTgtDevNumberOfLUs_Type())
scsiTgtDevNumberOfLUs.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiTgtDevNumberOfLUs.setStatus(_A)
class _ScsiTgtDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_S,1),(_c,2),(_d,3),(_e,4),(_f,5),('nonAddrFailure',6),('nonAddrFailReadying',7),('nonAddrFailAbnormal',8)))
_ScsiTgtDeviceStatus_Type.__name__=_N
_ScsiTgtDeviceStatus_Object=MibTableColumn
scsiTgtDeviceStatus=_ScsiTgtDeviceStatus_Object((1,3,6,1,2,1,999,1,4,1,1,2),_ScsiTgtDeviceStatus_Type())
scsiTgtDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiTgtDeviceStatus.setStatus(_A)
_ScsiTgtDevNonAccessibleLUs_Type=Gauge32
_ScsiTgtDevNonAccessibleLUs_Object=MibTableColumn
scsiTgtDevNonAccessibleLUs=_ScsiTgtDevNonAccessibleLUs_Object((1,3,6,1,2,1,999,1,4,1,1,3),_ScsiTgtDevNonAccessibleLUs_Type())
scsiTgtDevNonAccessibleLUs.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiTgtDevNonAccessibleLUs.setStatus(_A)
_ScsiTgtPortTable_Object=MibTable
scsiTgtPortTable=_ScsiTgtPortTable_Object((1,3,6,1,2,1,999,1,4,2))
if mibBuilder.loadTexts:scsiTgtPortTable.setStatus(_A)
_ScsiTgtPortEntry_Object=MibTableRow
scsiTgtPortEntry=_ScsiTgtPortEntry_Object((1,3,6,1,2,1,999,1,4,2,1))
scsiTgtPortEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_K))
if mibBuilder.loadTexts:scsiTgtPortEntry.setStatus(_A)
_ScsiTgtPortName_Type=ScsiName
_ScsiTgtPortName_Object=MibTableColumn
scsiTgtPortName=_ScsiTgtPortName_Object((1,3,6,1,2,1,999,1,4,2,1,1),_ScsiTgtPortName_Type())
scsiTgtPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiTgtPortName.setStatus(_A)
_ScsiTgtPortIdentifier_Type=ScsiIdentifier
_ScsiTgtPortIdentifier_Object=MibTableColumn
scsiTgtPortIdentifier=_ScsiTgtPortIdentifier_Object((1,3,6,1,2,1,999,1,4,2,1,2),_ScsiTgtPortIdentifier_Type())
scsiTgtPortIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiTgtPortIdentifier.setStatus(_A)
_ScsiTgtPortInCommands_Type=Counter32
_ScsiTgtPortInCommands_Object=MibTableColumn
scsiTgtPortInCommands=_ScsiTgtPortInCommands_Object((1,3,6,1,2,1,999,1,4,2,1,3),_ScsiTgtPortInCommands_Type())
scsiTgtPortInCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiTgtPortInCommands.setStatus(_A)
if mibBuilder.loadTexts:scsiTgtPortInCommands.setUnits(_G)
_ScsiTgtPortWrittenMegaBytes_Type=Counter32
_ScsiTgtPortWrittenMegaBytes_Object=MibTableColumn
scsiTgtPortWrittenMegaBytes=_ScsiTgtPortWrittenMegaBytes_Object((1,3,6,1,2,1,999,1,4,2,1,4),_ScsiTgtPortWrittenMegaBytes_Type())
scsiTgtPortWrittenMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiTgtPortWrittenMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:scsiTgtPortWrittenMegaBytes.setUnits(_H)
_ScsiTgtPortReadMegaBytes_Type=Counter32
_ScsiTgtPortReadMegaBytes_Object=MibTableColumn
scsiTgtPortReadMegaBytes=_ScsiTgtPortReadMegaBytes_Object((1,3,6,1,2,1,999,1,4,2,1,5),_ScsiTgtPortReadMegaBytes_Type())
scsiTgtPortReadMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiTgtPortReadMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:scsiTgtPortReadMegaBytes.setUnits(_H)
_ScsiTgtPortHSInCommands_Type=Counter64
_ScsiTgtPortHSInCommands_Object=MibTableColumn
scsiTgtPortHSInCommands=_ScsiTgtPortHSInCommands_Object((1,3,6,1,2,1,999,1,4,2,1,6),_ScsiTgtPortHSInCommands_Type())
scsiTgtPortHSInCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiTgtPortHSInCommands.setStatus(_A)
if mibBuilder.loadTexts:scsiTgtPortHSInCommands.setUnits(_G)
_ScsiRemoteInitiators_ObjectIdentity=ObjectIdentity
scsiRemoteInitiators=_ScsiRemoteInitiators_ObjectIdentity((1,3,6,1,2,1,999,1,4,3))
_ScsiAuthorizedIntrTable_Object=MibTable
scsiAuthorizedIntrTable=_ScsiAuthorizedIntrTable_Object((1,3,6,1,2,1,999,1,4,3,1))
if mibBuilder.loadTexts:scsiAuthorizedIntrTable.setStatus(_A)
_ScsiAuthorizedIntrEntry_Object=MibTableRow
scsiAuthorizedIntrEntry=_ScsiAuthorizedIntrEntry_Object((1,3,6,1,2,1,999,1,4,3,1,1))
scsiAuthorizedIntrEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:scsiAuthorizedIntrEntry.setStatus(_A)
_ScsiAuthIntrTgtPortIndex_Type=ScsiPortIndexValueOrZero
_ScsiAuthIntrTgtPortIndex_Object=MibTableColumn
scsiAuthIntrTgtPortIndex=_ScsiAuthIntrTgtPortIndex_Object((1,3,6,1,2,1,999,1,4,3,1,1,1),_ScsiAuthIntrTgtPortIndex_Type())
scsiAuthIntrTgtPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiAuthIntrTgtPortIndex.setStatus(_A)
_ScsiAuthIntrIndex_Type=ScsiIndexValue
_ScsiAuthIntrIndex_Object=MibTableColumn
scsiAuthIntrIndex=_ScsiAuthIntrIndex_Object((1,3,6,1,2,1,999,1,4,3,1,1,2),_ScsiAuthIntrIndex_Type())
scsiAuthIntrIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiAuthIntrIndex.setStatus(_A)
_ScsiAuthIntrDevOrPort_Type=ScsiDeviceOrPort
_ScsiAuthIntrDevOrPort_Object=MibTableColumn
scsiAuthIntrDevOrPort=_ScsiAuthIntrDevOrPort_Object((1,3,6,1,2,1,999,1,4,3,1,1,3),_ScsiAuthIntrDevOrPort_Type())
scsiAuthIntrDevOrPort.setMaxAccess(_I)
if mibBuilder.loadTexts:scsiAuthIntrDevOrPort.setStatus(_A)
_ScsiAuthIntrName_Type=ScsiName
_ScsiAuthIntrName_Object=MibTableColumn
scsiAuthIntrName=_ScsiAuthIntrName_Object((1,3,6,1,2,1,999,1,4,3,1,1,4),_ScsiAuthIntrName_Type())
scsiAuthIntrName.setMaxAccess(_I)
if mibBuilder.loadTexts:scsiAuthIntrName.setStatus(_A)
_ScsiAuthIntrLunMapIndex_Type=ScsiIndexValueOrZero
_ScsiAuthIntrLunMapIndex_Object=MibTableColumn
scsiAuthIntrLunMapIndex=_ScsiAuthIntrLunMapIndex_Object((1,3,6,1,2,1,999,1,4,3,1,1,5),_ScsiAuthIntrLunMapIndex_Type())
scsiAuthIntrLunMapIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:scsiAuthIntrLunMapIndex.setStatus(_A)
_ScsiAuthIntrAttachedTimes_Type=Counter32
_ScsiAuthIntrAttachedTimes_Object=MibTableColumn
scsiAuthIntrAttachedTimes=_ScsiAuthIntrAttachedTimes_Object((1,3,6,1,2,1,999,1,4,3,1,1,6),_ScsiAuthIntrAttachedTimes_Type())
scsiAuthIntrAttachedTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiAuthIntrAttachedTimes.setStatus(_A)
if mibBuilder.loadTexts:scsiAuthIntrAttachedTimes.setUnits('Times')
_ScsiAuthIntrOutCommands_Type=Counter32
_ScsiAuthIntrOutCommands_Object=MibTableColumn
scsiAuthIntrOutCommands=_ScsiAuthIntrOutCommands_Object((1,3,6,1,2,1,999,1,4,3,1,1,7),_ScsiAuthIntrOutCommands_Type())
scsiAuthIntrOutCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiAuthIntrOutCommands.setStatus(_A)
if mibBuilder.loadTexts:scsiAuthIntrOutCommands.setUnits(_G)
_ScsiAuthIntrReadMegaBytes_Type=Counter32
_ScsiAuthIntrReadMegaBytes_Object=MibTableColumn
scsiAuthIntrReadMegaBytes=_ScsiAuthIntrReadMegaBytes_Object((1,3,6,1,2,1,999,1,4,3,1,1,8),_ScsiAuthIntrReadMegaBytes_Type())
scsiAuthIntrReadMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiAuthIntrReadMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:scsiAuthIntrReadMegaBytes.setUnits(_H)
_ScsiAuthIntrWrittenMegaBytes_Type=Counter32
_ScsiAuthIntrWrittenMegaBytes_Object=MibTableColumn
scsiAuthIntrWrittenMegaBytes=_ScsiAuthIntrWrittenMegaBytes_Object((1,3,6,1,2,1,999,1,4,3,1,1,9),_ScsiAuthIntrWrittenMegaBytes_Type())
scsiAuthIntrWrittenMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiAuthIntrWrittenMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:scsiAuthIntrWrittenMegaBytes.setUnits(_H)
_ScsiAuthIntrHSOutCommands_Type=Counter64
_ScsiAuthIntrHSOutCommands_Object=MibTableColumn
scsiAuthIntrHSOutCommands=_ScsiAuthIntrHSOutCommands_Object((1,3,6,1,2,1,999,1,4,3,1,1,10),_ScsiAuthIntrHSOutCommands_Type())
scsiAuthIntrHSOutCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiAuthIntrHSOutCommands.setStatus(_A)
if mibBuilder.loadTexts:scsiAuthIntrHSOutCommands.setUnits(_G)
_ScsiAuthIntrLastCreation_Type=TimeStamp
_ScsiAuthIntrLastCreation_Object=MibTableColumn
scsiAuthIntrLastCreation=_ScsiAuthIntrLastCreation_Object((1,3,6,1,2,1,999,1,4,3,1,1,11),_ScsiAuthIntrLastCreation_Type())
scsiAuthIntrLastCreation.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiAuthIntrLastCreation.setStatus(_A)
_ScsiAuthIntrRowStatus_Type=RowStatus
_ScsiAuthIntrRowStatus_Object=MibTableColumn
scsiAuthIntrRowStatus=_ScsiAuthIntrRowStatus_Object((1,3,6,1,2,1,999,1,4,3,1,1,12),_ScsiAuthIntrRowStatus_Type())
scsiAuthIntrRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:scsiAuthIntrRowStatus.setStatus(_A)
_ScsiAttIntrPrtTable_Object=MibTable
scsiAttIntrPrtTable=_ScsiAttIntrPrtTable_Object((1,3,6,1,2,1,999,1,4,3,2))
if mibBuilder.loadTexts:scsiAttIntrPrtTable.setStatus(_A)
_ScsiAttIntrPrtEntry_Object=MibTableRow
scsiAttIntrPrtEntry=_ScsiAttIntrPrtEntry_Object((1,3,6,1,2,1,999,1,4,3,2,1))
scsiAttIntrPrtEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_K),(0,_B,_i))
if mibBuilder.loadTexts:scsiAttIntrPrtEntry.setStatus(_A)
_ScsiAttIntrPrtIdx_Type=ScsiIndexValue
_ScsiAttIntrPrtIdx_Object=MibTableColumn
scsiAttIntrPrtIdx=_ScsiAttIntrPrtIdx_Object((1,3,6,1,2,1,999,1,4,3,2,1,1),_ScsiAttIntrPrtIdx_Type())
scsiAttIntrPrtIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiAttIntrPrtIdx.setStatus(_A)
_ScsiAttIntrPrtAuthIntrIdx_Type=ScsiIndexValueOrZero
_ScsiAttIntrPrtAuthIntrIdx_Object=MibTableColumn
scsiAttIntrPrtAuthIntrIdx=_ScsiAttIntrPrtAuthIntrIdx_Object((1,3,6,1,2,1,999,1,4,3,2,1,2),_ScsiAttIntrPrtAuthIntrIdx_Type())
scsiAttIntrPrtAuthIntrIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiAttIntrPrtAuthIntrIdx.setStatus(_A)
_ScsiAttIntrPrtName_Type=ScsiName
_ScsiAttIntrPrtName_Object=MibTableColumn
scsiAttIntrPrtName=_ScsiAttIntrPrtName_Object((1,3,6,1,2,1,999,1,4,3,2,1,3),_ScsiAttIntrPrtName_Type())
scsiAttIntrPrtName.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiAttIntrPrtName.setStatus(_A)
_ScsiAttIntrPrtId_Type=ScsiIdentifier
_ScsiAttIntrPrtId_Object=MibTableColumn
scsiAttIntrPrtId=_ScsiAttIntrPrtId_Object((1,3,6,1,2,1,999,1,4,3,2,1,4),_ScsiAttIntrPrtId_Type())
scsiAttIntrPrtId.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiAttIntrPrtId.setStatus(_A)
_ScsiLogicalUnit_ObjectIdentity=ObjectIdentity
scsiLogicalUnit=_ScsiLogicalUnit_ObjectIdentity((1,3,6,1,2,1,999,1,5))
_ScsiLuTable_Object=MibTable
scsiLuTable=_ScsiLuTable_Object((1,3,6,1,2,1,999,1,5,1))
if mibBuilder.loadTexts:scsiLuTable.setStatus(_A)
_ScsiLuEntry_Object=MibTableRow
scsiLuEntry=_ScsiLuEntry_Object((1,3,6,1,2,1,999,1,5,1,1))
scsiLuEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_U))
if mibBuilder.loadTexts:scsiLuEntry.setStatus(_A)
_ScsiLuIndex_Type=ScsiIndexValue
_ScsiLuIndex_Object=MibTableColumn
scsiLuIndex=_ScsiLuIndex_Object((1,3,6,1,2,1,999,1,5,1,1,1),_ScsiLuIndex_Type())
scsiLuIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiLuIndex.setStatus(_A)
_ScsiLuDefaultLun_Type=ScsiLUNOrZero
_ScsiLuDefaultLun_Object=MibTableColumn
scsiLuDefaultLun=_ScsiLuDefaultLun_Object((1,3,6,1,2,1,999,1,5,1,1,2),_ScsiLuDefaultLun_Type())
scsiLuDefaultLun.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuDefaultLun.setStatus(_A)
_ScsiLuWwnName_Type=ScsiNameIdOrZero
_ScsiLuWwnName_Object=MibTableColumn
scsiLuWwnName=_ScsiLuWwnName_Object((1,3,6,1,2,1,999,1,5,1,1,3),_ScsiLuWwnName_Type())
scsiLuWwnName.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuWwnName.setStatus(_A)
class _ScsiLuVendorId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ScsiLuVendorId_Type.__name__=_J
_ScsiLuVendorId_Object=MibTableColumn
scsiLuVendorId=_ScsiLuVendorId_Object((1,3,6,1,2,1,999,1,5,1,1,4),_ScsiLuVendorId_Type())
scsiLuVendorId.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuVendorId.setStatus(_A)
class _ScsiLuProductId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ScsiLuProductId_Type.__name__=_J
_ScsiLuProductId_Object=MibTableColumn
scsiLuProductId=_ScsiLuProductId_Object((1,3,6,1,2,1,999,1,5,1,1,5),_ScsiLuProductId_Type())
scsiLuProductId.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuProductId.setStatus(_A)
class _ScsiLuRevisionId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,79))
_ScsiLuRevisionId_Type.__name__=_J
_ScsiLuRevisionId_Object=MibTableColumn
scsiLuRevisionId=_ScsiLuRevisionId_Object((1,3,6,1,2,1,999,1,5,1,1,6),_ScsiLuRevisionId_Type())
scsiLuRevisionId.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuRevisionId.setStatus(_A)
_ScsiLuPeripheralType_Type=Unsigned32
_ScsiLuPeripheralType_Object=MibTableColumn
scsiLuPeripheralType=_ScsiLuPeripheralType_Object((1,3,6,1,2,1,999,1,5,1,1,7),_ScsiLuPeripheralType_Type())
scsiLuPeripheralType.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuPeripheralType.setStatus(_A)
class _ScsiLuStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_S,1),(_c,2),('notAvailable',3),(_d,4),(_e,5),(_f,6)))
_ScsiLuStatus_Type.__name__=_N
_ScsiLuStatus_Object=MibTableColumn
scsiLuStatus=_ScsiLuStatus_Object((1,3,6,1,2,1,999,1,5,1,1,8),_ScsiLuStatus_Type())
scsiLuStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuStatus.setStatus(_A)
class _ScsiLuState_Type(Bits):namedValues=NamedValues(*(('dataLost',0),('dynamicReconfigurationInProgress',1),('exposed',2),('fractionallyExposed',3),('partiallyExposed',4),('protectedRebuild',5),('protectionDisabled',6),('rebuild',7),('recalculate',8),('spareInUse',9),('verifyInProgress',10)))
_ScsiLuState_Type.__name__=_M
_ScsiLuState_Object=MibTableColumn
scsiLuState=_ScsiLuState_Object((1,3,6,1,2,1,999,1,5,1,1,9),_ScsiLuState_Type())
scsiLuState.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuState.setStatus(_A)
_ScsiLuInCommands_Type=Counter32
_ScsiLuInCommands_Object=MibTableColumn
scsiLuInCommands=_ScsiLuInCommands_Object((1,3,6,1,2,1,999,1,5,1,1,10),_ScsiLuInCommands_Type())
scsiLuInCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuInCommands.setStatus(_A)
if mibBuilder.loadTexts:scsiLuInCommands.setUnits(_G)
_ScsiLuReadMegaBytes_Type=Counter32
_ScsiLuReadMegaBytes_Object=MibTableColumn
scsiLuReadMegaBytes=_ScsiLuReadMegaBytes_Object((1,3,6,1,2,1,999,1,5,1,1,11),_ScsiLuReadMegaBytes_Type())
scsiLuReadMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuReadMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:scsiLuReadMegaBytes.setUnits(_H)
_ScsiLuWrittenMegaBytes_Type=Counter32
_ScsiLuWrittenMegaBytes_Object=MibTableColumn
scsiLuWrittenMegaBytes=_ScsiLuWrittenMegaBytes_Object((1,3,6,1,2,1,999,1,5,1,1,12),_ScsiLuWrittenMegaBytes_Type())
scsiLuWrittenMegaBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuWrittenMegaBytes.setStatus(_A)
if mibBuilder.loadTexts:scsiLuWrittenMegaBytes.setUnits(_H)
_ScsiLuInResets_Type=Counter32
_ScsiLuInResets_Object=MibTableColumn
scsiLuInResets=_ScsiLuInResets_Object((1,3,6,1,2,1,999,1,5,1,1,13),_ScsiLuInResets_Type())
scsiLuInResets.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuInResets.setStatus(_A)
if mibBuilder.loadTexts:scsiLuInResets.setUnits('resets')
_ScsiLuOutQueueFullStatus_Type=Counter32
_ScsiLuOutQueueFullStatus_Object=MibTableColumn
scsiLuOutQueueFullStatus=_ScsiLuOutQueueFullStatus_Object((1,3,6,1,2,1,999,1,5,1,1,14),_ScsiLuOutQueueFullStatus_Type())
scsiLuOutQueueFullStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuOutQueueFullStatus.setStatus(_A)
_ScsiLuHSInCommands_Type=Counter64
_ScsiLuHSInCommands_Object=MibTableColumn
scsiLuHSInCommands=_ScsiLuHSInCommands_Object((1,3,6,1,2,1,999,1,5,1,1,15),_ScsiLuHSInCommands_Type())
scsiLuHSInCommands.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuHSInCommands.setStatus(_A)
if mibBuilder.loadTexts:scsiLuHSInCommands.setUnits(_G)
_ScsiLuIdTable_Object=MibTable
scsiLuIdTable=_ScsiLuIdTable_Object((1,3,6,1,2,1,999,1,5,2))
if mibBuilder.loadTexts:scsiLuIdTable.setStatus(_A)
_ScsiLuIdEntry_Object=MibTableRow
scsiLuIdEntry=_ScsiLuIdEntry_Object((1,3,6,1,2,1,999,1,5,2,1))
scsiLuIdEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_U),(0,_B,_j))
if mibBuilder.loadTexts:scsiLuIdEntry.setStatus(_A)
_ScsiLuIdIndex_Type=ScsiIndexValue
_ScsiLuIdIndex_Object=MibTableColumn
scsiLuIdIndex=_ScsiLuIdIndex_Object((1,3,6,1,2,1,999,1,5,2,1,1),_ScsiLuIdIndex_Type())
scsiLuIdIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiLuIdIndex.setStatus(_A)
_ScsiLuIdCodeSet_Type=ScsiIdCodeSet
_ScsiLuIdCodeSet_Object=MibTableColumn
scsiLuIdCodeSet=_ScsiLuIdCodeSet_Object((1,3,6,1,2,1,999,1,5,2,1,2),_ScsiLuIdCodeSet_Type())
scsiLuIdCodeSet.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuIdCodeSet.setStatus(_A)
_ScsiLuIdAssociation_Type=ScsiIdAssociation
_ScsiLuIdAssociation_Object=MibTableColumn
scsiLuIdAssociation=_ScsiLuIdAssociation_Object((1,3,6,1,2,1,999,1,5,2,1,3),_ScsiLuIdAssociation_Type())
scsiLuIdAssociation.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuIdAssociation.setStatus(_A)
_ScsiLuIdType_Type=ScsiIdType
_ScsiLuIdType_Object=MibTableColumn
scsiLuIdType=_ScsiLuIdType_Object((1,3,6,1,2,1,999,1,5,2,1,4),_ScsiLuIdType_Type())
scsiLuIdType.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuIdType.setStatus(_A)
_ScsiLuIdValue_Type=ScsiIdValue
_ScsiLuIdValue_Object=MibTableColumn
scsiLuIdValue=_ScsiLuIdValue_Object((1,3,6,1,2,1,999,1,5,2,1,5),_ScsiLuIdValue_Type())
scsiLuIdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:scsiLuIdValue.setStatus(_A)
_ScsiLunMapTable_Object=MibTable
scsiLunMapTable=_ScsiLunMapTable_Object((1,3,6,1,2,1,999,1,5,3))
if mibBuilder.loadTexts:scsiLunMapTable.setStatus(_A)
_ScsiLunMapEntry_Object=MibTableRow
scsiLunMapEntry=_ScsiLunMapEntry_Object((1,3,6,1,2,1,999,1,5,3,1))
scsiLunMapEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_k),(0,_B,_l))
if mibBuilder.loadTexts:scsiLunMapEntry.setStatus(_A)
_ScsiLunMapIndex_Type=ScsiIndexValue
_ScsiLunMapIndex_Object=MibTableColumn
scsiLunMapIndex=_ScsiLunMapIndex_Object((1,3,6,1,2,1,999,1,5,3,1,1),_ScsiLunMapIndex_Type())
scsiLunMapIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiLunMapIndex.setStatus(_A)
_ScsiLunMapLun_Type=ScsiLUNOrZero
_ScsiLunMapLun_Object=MibTableColumn
scsiLunMapLun=_ScsiLunMapLun_Object((1,3,6,1,2,1,999,1,5,3,1,2),_ScsiLunMapLun_Type())
scsiLunMapLun.setMaxAccess(_F)
if mibBuilder.loadTexts:scsiLunMapLun.setStatus(_A)
_ScsiLunMapLuIndex_Type=ScsiIndexValue
_ScsiLunMapLuIndex_Object=MibTableColumn
scsiLunMapLuIndex=_ScsiLunMapLuIndex_Object((1,3,6,1,2,1,999,1,5,3,1,3),_ScsiLunMapLuIndex_Type())
scsiLunMapLuIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:scsiLunMapLuIndex.setStatus(_A)
_ScsiLunMapRowStatus_Type=RowStatus
_ScsiLunMapRowStatus_Object=MibTableColumn
scsiLunMapRowStatus=_ScsiLunMapRowStatus_Object((1,3,6,1,2,1,999,1,5,3,1,4),_ScsiLunMapRowStatus_Type())
scsiLunMapRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:scsiLunMapRowStatus.setStatus(_A)
_ScsiNotifications_ObjectIdentity=ObjectIdentity
scsiNotifications=_ScsiNotifications_ObjectIdentity((1,3,6,1,2,1,999,2))
_ScsiNotificationsPrefix_ObjectIdentity=ObjectIdentity
scsiNotificationsPrefix=_ScsiNotificationsPrefix_ObjectIdentity((1,3,6,1,2,1,999,2,0))
_ScsiConformance_ObjectIdentity=ObjectIdentity
scsiConformance=_ScsiConformance_ObjectIdentity((1,3,6,1,2,1,999,3))
_ScsiCompliances_ObjectIdentity=ObjectIdentity
scsiCompliances=_ScsiCompliances_ObjectIdentity((1,3,6,1,2,1,999,3,1))
_ScsiGroups_ObjectIdentity=ObjectIdentity
scsiGroups=_ScsiGroups_ObjectIdentity((1,3,6,1,2,1,999,3,2))
scsiDeviceGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,1))
scsiDeviceGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:scsiDeviceGroup.setStatus(_A)
scsiInitiatorGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,2))
scsiInitiatorGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:scsiInitiatorGroup.setStatus(_A)
scsiDiscoveryGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,3))
scsiDiscoveryGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:scsiDiscoveryGroup.setStatus(_A)
scsiTargetGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,4))
scsiTargetGroup.setObjects(*((_B,_AF),(_B,_V),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_W),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW)))
if mibBuilder.loadTexts:scsiTargetGroup.setStatus(_A)
scsiLunMapGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,5))
scsiLunMapGroup.setObjects(*((_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:scsiLunMapGroup.setStatus(_A)
scsiTargetStatsGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,6))
scsiTargetStatsGroup.setObjects(*((_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al)))
if mibBuilder.loadTexts:scsiTargetStatsGroup.setStatus(_A)
scsiTargetHSStatsGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,7))
scsiTargetHSStatsGroup.setObjects(*((_B,_Am),(_B,_An)))
if mibBuilder.loadTexts:scsiTargetHSStatsGroup.setStatus(_A)
scsiLunMapStatsGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,8))
scsiLunMapStatsGroup.setObjects(*((_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar)))
if mibBuilder.loadTexts:scsiLunMapStatsGroup.setStatus(_A)
scsiLunMapHSStatsGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,9))
scsiLunMapHSStatsGroup.setObjects((_B,_As))
if mibBuilder.loadTexts:scsiLunMapHSStatsGroup.setStatus(_A)
scsiInitiatorStatsGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,10))
scsiInitiatorStatsGroup.setObjects(*((_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw)))
if mibBuilder.loadTexts:scsiInitiatorStatsGroup.setStatus(_A)
scsiInitiatorHSStatsGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,11))
scsiInitiatorHSStatsGroup.setObjects((_B,_Ax))
if mibBuilder.loadTexts:scsiInitiatorHSStatsGroup.setStatus(_A)
scsiDiscoveryStatsGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,12))
scsiDiscoveryStatsGroup.setObjects(*((_B,_Ay),(_B,_Az),(_B,_A_)))
if mibBuilder.loadTexts:scsiDiscoveryStatsGroup.setStatus(_A)
scsiDiscoveryHSStatsGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,13))
scsiDiscoveryHSStatsGroup.setObjects((_B,_B0))
if mibBuilder.loadTexts:scsiDiscoveryHSStatsGroup.setStatus(_A)
scsiDeviceStatGroup=ObjectGroup((1,3,6,1,2,1,999,3,2,14))
scsiDeviceStatGroup.setObjects(*((_B,_B1),(_B,_B2)))
if mibBuilder.loadTexts:scsiDeviceStatGroup.setStatus(_A)
scsiTgtDeviceStatusChanged=NotificationType((1,3,6,1,2,1,999,2,0,1))
scsiTgtDeviceStatusChanged.setObjects((_B,_V))
if mibBuilder.loadTexts:scsiTgtDeviceStatusChanged.setStatus(_A)
scsiLuStatusChanged=NotificationType((1,3,6,1,2,1,999,2,0,2))
scsiLuStatusChanged.setObjects((_B,_W))
if mibBuilder.loadTexts:scsiLuStatusChanged.setStatus(_A)
scsiCompliance=ModuleCompliance((1,3,6,1,2,1,999,3,1,1))
scsiCompliance.setObjects((_B,_B3))
if mibBuilder.loadTexts:scsiCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ScsiLUNOrZero':ScsiLUNOrZero,'ScsiIndexValue':ScsiIndexValue,'ScsiPortIndexValueOrZero':ScsiPortIndexValueOrZero,'ScsiIndexValueOrZero':ScsiIndexValueOrZero,'ScsiIdentifier':ScsiIdentifier,'ScsiName':ScsiName,'ScsiNameIdOrZero':ScsiNameIdOrZero,'ScsiDeviceOrPort':ScsiDeviceOrPort,'ScsiIdCodeSet':ScsiIdCodeSet,'ScsiIdAssociation':ScsiIdAssociation,'ScsiIdType':ScsiIdType,'ScsiIdValue':ScsiIdValue,'HrSWInstalledIndexOrZero':HrSWInstalledIndexOrZero,'scsiModule':scsiModule,'scsiObjects':scsiObjects,'scsiTransportTypes':scsiTransportTypes,'scsiTranportOther':scsiTranportOther,'scsiTranportSPI':scsiTranportSPI,'scsiTransportFCP':scsiTransportFCP,'scsiTransportSRP':scsiTransportSRP,'scsiTransportISCSI':scsiTransportISCSI,'scsiTransportSBP':scsiTransportSBP,'scsiGeneral':scsiGeneral,'scsiInstanceTable':scsiInstanceTable,'scsiInstanceEntry':scsiInstanceEntry,_D:scsiInstIndex,_m:scsiInstAlias,_n:scsiInstSoftwareIndex,_o:scsiInstVendorVersion,_p:scsiInstScsiNotificationsEnable,'scsiDeviceTable':scsiDeviceTable,'scsiDeviceEntry':scsiDeviceEntry,_E:scsiDeviceIndex,_q:scsiDeviceAlias,_r:scsiDeviceRole,_s:scsiDevicePortNumber,_B1:scsiDeviceResets,'scsiPortTable':scsiPortTable,'scsiPortEntry':scsiPortEntry,_K:scsiPortIndex,_t:scsiPortRole,_u:scsiPortTrnsptPtr,_B2:scsiPortBusyStatuses,'scsiTrnsptTable':scsiTrnsptTable,'scsiTrnsptEntry':scsiTrnsptEntry,_Z:scsiTrnsptIndex,_v:scsiTrnsptType,_w:scsiTrnsptPointer,_x:scsiTrnsptDevName,'scsiInitiator':scsiInitiator,'scsiIntrDevTable':scsiIntrDevTable,'scsiIntrDevEntry':scsiIntrDevEntry,_y:scsiIntrDevTgtAccessMode,_At:scsiIntrDevOutResets,'scsiIntrPrtTable':scsiIntrPrtTable,'scsiIntrPrtEntry':scsiIntrPrtEntry,_z:scsiIntrPrtName,_A0:scsiIntrPrtIdentifier,_Au:scsiIntrPrtOutCommands,_Av:scsiIntrPrtWrittenMegaBytes,_Aw:scsiIntrPrtReadMegaBytes,_Ax:scsiIntrPrtHSOutCommands,'scsiRemoteTarget':scsiRemoteTarget,'scsiDscTgtTable':scsiDscTgtTable,'scsiDscTgtEntry':scsiDscTgtEntry,_P:scsiDscTgtIntrPortIndex,_Q:scsiDscTgtIndex,_A4:scsiDscTgtDevOrPort,_A5:scsiDscTgtName,_A6:scsiDscTgtConfigured,_A7:scsiDscTgtDiscovered,_Ay:scsiDscTgtInCommands,_A_:scsiDscTgtWrittenMegaBytes,_Az:scsiDscTgtReadMegaBytes,_B0:scsiDscTgtHSInCommands,_A9:scsiDscTgtLastCreation,_A8:scsiDscTgtRowStatus,'scsiDscLunTable':scsiDscLunTable,'scsiDscLunEntry':scsiDscLunEntry,_T:scsiDscLunIndex,_AA:scsiDscLunLun,'scsiDscLunIdTable':scsiDscLunIdTable,'scsiDscLunIdEntry':scsiDscLunIdEntry,_a:scsiDscLunIdIndex,_AB:scsiDscLunIdCodeSet,_AC:scsiDscLunIdAssociation,_AD:scsiDscLunIdType,_AE:scsiDscLunIdValue,'scsiAttTgtPortTable':scsiAttTgtPortTable,'scsiAttTgtPortEntry':scsiAttTgtPortEntry,_b:scsiAttTgtPortIndex,_A1:scsiAttTgtPortDscTgtIdx,_A2:scsiAttTgtPortName,_A3:scsiAttTgtPortIdentifier,'scsiTarget':scsiTarget,'scsiTgtDevTable':scsiTgtDevTable,'scsiTgtDevEntry':scsiTgtDevEntry,_AF:scsiTgtDevNumberOfLUs,_V:scsiTgtDeviceStatus,_AG:scsiTgtDevNonAccessibleLUs,'scsiTgtPortTable':scsiTgtPortTable,'scsiTgtPortEntry':scsiTgtPortEntry,_AH:scsiTgtPortName,_AI:scsiTgtPortIdentifier,_Ae:scsiTgtPortInCommands,_Af:scsiTgtPortWrittenMegaBytes,_Ag:scsiTgtPortReadMegaBytes,_Am:scsiTgtPortHSInCommands,'scsiRemoteInitiators':scsiRemoteInitiators,'scsiAuthorizedIntrTable':scsiAuthorizedIntrTable,'scsiAuthorizedIntrEntry':scsiAuthorizedIntrEntry,_g:scsiAuthIntrTgtPortIndex,_h:scsiAuthIntrIndex,_AZ:scsiAuthIntrDevOrPort,_Aa:scsiAuthIntrName,_Ab:scsiAuthIntrLunMapIndex,_Ao:scsiAuthIntrAttachedTimes,_Ap:scsiAuthIntrOutCommands,_Aq:scsiAuthIntrReadMegaBytes,_Ar:scsiAuthIntrWrittenMegaBytes,_As:scsiAuthIntrHSOutCommands,_Ac:scsiAuthIntrLastCreation,_Ad:scsiAuthIntrRowStatus,'scsiAttIntrPrtTable':scsiAttIntrPrtTable,'scsiAttIntrPrtEntry':scsiAttIntrPrtEntry,_i:scsiAttIntrPrtIdx,_AJ:scsiAttIntrPrtAuthIntrIdx,_AK:scsiAttIntrPrtName,_AL:scsiAttIntrPrtId,'scsiLogicalUnit':scsiLogicalUnit,'scsiLuTable':scsiLuTable,'scsiLuEntry':scsiLuEntry,_U:scsiLuIndex,_AM:scsiLuDefaultLun,_AN:scsiLuWwnName,_AO:scsiLuVendorId,_AP:scsiLuProductId,_AQ:scsiLuRevisionId,_AR:scsiLuPeripheralType,_W:scsiLuStatus,_AS:scsiLuState,_Ah:scsiLuInCommands,_Ai:scsiLuReadMegaBytes,_Aj:scsiLuWrittenMegaBytes,_Ak:scsiLuInResets,_Al:scsiLuOutQueueFullStatus,_An:scsiLuHSInCommands,'scsiLuIdTable':scsiLuIdTable,'scsiLuIdEntry':scsiLuIdEntry,_j:scsiLuIdIndex,_AT:scsiLuIdCodeSet,_AU:scsiLuIdAssociation,_AV:scsiLuIdType,_AW:scsiLuIdValue,'scsiLunMapTable':scsiLunMapTable,'scsiLunMapEntry':scsiLunMapEntry,_k:scsiLunMapIndex,_l:scsiLunMapLun,_AX:scsiLunMapLuIndex,_AY:scsiLunMapRowStatus,'scsiNotifications':scsiNotifications,'scsiNotificationsPrefix':scsiNotificationsPrefix,'scsiTgtDeviceStatusChanged':scsiTgtDeviceStatusChanged,'scsiLuStatusChanged':scsiLuStatusChanged,'scsiConformance':scsiConformance,'scsiCompliances':scsiCompliances,'scsiCompliance':scsiCompliance,'scsiGroups':scsiGroups,_B3:scsiDeviceGroup,'scsiInitiatorGroup':scsiInitiatorGroup,'scsiDiscoveryGroup':scsiDiscoveryGroup,'scsiTargetGroup':scsiTargetGroup,'scsiLunMapGroup':scsiLunMapGroup,'scsiTargetStatsGroup':scsiTargetStatsGroup,'scsiTargetHSStatsGroup':scsiTargetHSStatsGroup,'scsiLunMapStatsGroup':scsiLunMapStatsGroup,'scsiLunMapHSStatsGroup':scsiLunMapHSStatsGroup,'scsiInitiatorStatsGroup':scsiInitiatorStatsGroup,'scsiInitiatorHSStatsGroup':scsiInitiatorHSStatsGroup,'scsiDiscoveryStatsGroup':scsiDiscoveryStatsGroup,'scsiDiscoveryHSStatsGroup':scsiDiscoveryHSStatsGroup,'scsiDeviceStatGroup':scsiDeviceStatGroup})