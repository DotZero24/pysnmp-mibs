_n='cfdmiNotificationGroup'
_m='cfdmiHbaPortInformationGroup'
_l='cfdmiHbaInformationGroup'
_k='cfdmiConfigGroup'
_j='cfdmiRejectRegNotify'
_i='cfdmiHbaPortHostName'
_h='cfdmiHbaPortOsDevName'
_g='cfdmiHbaPortMaxFrameSize'
_f='cfdmiHbaPortCurrentSpeed'
_e='cfdmiHbaPortSupportedSpeed'
_d='cfdmiHbaPortSupportedFC4Type'
_c='cfdmiHbaInfoMaxCTPayload'
_b='cfdmiHbaInfoOSInfo'
_a='cfdmiHbaInfoFwVer'
_Z='cfdmiHbaInfoOptROMVer'
_Y='cfdmiHbaInfoDriverVer'
_X='cfdmiHbaInfoHwVer'
_W='cfdmiHbaInfoModelDescr'
_V='cfdmiHbaInfoModel'
_U='cfdmiHbaInfoSn'
_T='cfdmiHbaInfoMfg'
_S='cfdmiHbaInfoNodeName'
_R='cfdmiRejectRegNotifyEnable'
_Q='cfdmiHbaPortId'
_P='not-accessible'
_O='TruthValue'
_N='Integer32'
_M='notifyVsanIndex'
_L='cfdmiNotifyHBAPortId'
_K='cfdmiNotifyRegOperType'
_J='cfdmiRejectReasonCodeExpl'
_I='cfdmiRejectReasonCode'
_H='cfdmiHbaInfoId'
_G='vsanIndex'
_F='accessible-for-notify'
_E='CISCO-VSAN-MIB'
_D='SnmpAdminString'
_C='read-only'
_B='CISCO-FDMI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
FcNameId,=mibBuilder.importSymbols('CISCO-ST-TC','FcNameId')
notifyVsanIndex,vsanIndex=mibBuilder.importSymbols(_E,_M,_G)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_O)
ciscoFdmiMIB=ModuleIdentity((1,3,6,1,4,1,9,9,373))
if mibBuilder.loadTexts:ciscoFdmiMIB.setRevisions(('2003-11-07 00:00','2003-08-24 00:00'))
class CFdmiRejectReasonCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalidCommandCode',1),('unableToPerformCmdReq',2),('invalidSize',3)))
class CFdmiRejectReasonCodeExpl(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('noAdditionalExpl',1),('hbaAlreadyRegistered',2),('attrForSpecifiedHbaNotReg',3),('hbaAttrMultiAttribSameType',4),('invalidHbaAttrBlockLen',5),('reqdHbaAttrNotPresent',6),('origPortNotInRegPortList',7),('hbaIdNotInRegPortList',8),('portAttrNotRegistered',9),('portNotRegistered',10),('portAttrMultiAttrSameType',11),('invalidPortAttrBlockLen',12),('none',13)))
_CiscoFdmiMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoFdmiMIBNotifications=_CiscoFdmiMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,373,0))
_CiscoFdmiMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFdmiMIBObjects=_CiscoFdmiMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,373,1))
_CfdmiConfig_ObjectIdentity=ObjectIdentity
cfdmiConfig=_CfdmiConfig_ObjectIdentity((1,3,6,1,4,1,9,9,373,1,1))
class _CfdmiRejectRegNotifyEnable_Type(TruthValue):defaultValue=2
_CfdmiRejectRegNotifyEnable_Type.__name__=_O
_CfdmiRejectRegNotifyEnable_Object=MibScalar
cfdmiRejectRegNotifyEnable=_CfdmiRejectRegNotifyEnable_Object((1,3,6,1,4,1,9,9,373,1,1,1),_CfdmiRejectRegNotifyEnable_Type())
cfdmiRejectRegNotifyEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cfdmiRejectRegNotifyEnable.setStatus(_A)
_CfdmiInfo_ObjectIdentity=ObjectIdentity
cfdmiInfo=_CfdmiInfo_ObjectIdentity((1,3,6,1,4,1,9,9,373,1,2))
_CfdmiHbaInfoTable_Object=MibTable
cfdmiHbaInfoTable=_CfdmiHbaInfoTable_Object((1,3,6,1,4,1,9,9,373,1,2,1))
if mibBuilder.loadTexts:cfdmiHbaInfoTable.setStatus(_A)
_CfdmiHbaInfoEntry_Object=MibTableRow
cfdmiHbaInfoEntry=_CfdmiHbaInfoEntry_Object((1,3,6,1,4,1,9,9,373,1,2,1,1))
cfdmiHbaInfoEntry.setIndexNames((0,_E,_G),(0,_B,_H))
if mibBuilder.loadTexts:cfdmiHbaInfoEntry.setStatus(_A)
_CfdmiHbaInfoId_Type=FcNameId
_CfdmiHbaInfoId_Object=MibTableColumn
cfdmiHbaInfoId=_CfdmiHbaInfoId_Object((1,3,6,1,4,1,9,9,373,1,2,1,1,1),_CfdmiHbaInfoId_Type())
cfdmiHbaInfoId.setMaxAccess(_P)
if mibBuilder.loadTexts:cfdmiHbaInfoId.setStatus(_A)
_CfdmiHbaInfoNodeName_Type=FcNameId
_CfdmiHbaInfoNodeName_Object=MibTableColumn
cfdmiHbaInfoNodeName=_CfdmiHbaInfoNodeName_Object((1,3,6,1,4,1,9,9,373,1,2,1,1,2),_CfdmiHbaInfoNodeName_Type())
cfdmiHbaInfoNodeName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaInfoNodeName.setStatus(_A)
class _CfdmiHbaInfoMfg_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CfdmiHbaInfoMfg_Type.__name__=_D
_CfdmiHbaInfoMfg_Object=MibTableColumn
cfdmiHbaInfoMfg=_CfdmiHbaInfoMfg_Object((1,3,6,1,4,1,9,9,373,1,2,1,1,3),_CfdmiHbaInfoMfg_Type())
cfdmiHbaInfoMfg.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaInfoMfg.setStatus(_A)
class _CfdmiHbaInfoSn_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CfdmiHbaInfoSn_Type.__name__=_D
_CfdmiHbaInfoSn_Object=MibTableColumn
cfdmiHbaInfoSn=_CfdmiHbaInfoSn_Object((1,3,6,1,4,1,9,9,373,1,2,1,1,4),_CfdmiHbaInfoSn_Type())
cfdmiHbaInfoSn.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaInfoSn.setStatus(_A)
class _CfdmiHbaInfoModel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CfdmiHbaInfoModel_Type.__name__=_D
_CfdmiHbaInfoModel_Object=MibTableColumn
cfdmiHbaInfoModel=_CfdmiHbaInfoModel_Object((1,3,6,1,4,1,9,9,373,1,2,1,1,5),_CfdmiHbaInfoModel_Type())
cfdmiHbaInfoModel.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaInfoModel.setStatus(_A)
class _CfdmiHbaInfoModelDescr_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CfdmiHbaInfoModelDescr_Type.__name__=_D
_CfdmiHbaInfoModelDescr_Object=MibTableColumn
cfdmiHbaInfoModelDescr=_CfdmiHbaInfoModelDescr_Object((1,3,6,1,4,1,9,9,373,1,2,1,1,6),_CfdmiHbaInfoModelDescr_Type())
cfdmiHbaInfoModelDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaInfoModelDescr.setStatus(_A)
class _CfdmiHbaInfoHwVer_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CfdmiHbaInfoHwVer_Type.__name__=_D
_CfdmiHbaInfoHwVer_Object=MibTableColumn
cfdmiHbaInfoHwVer=_CfdmiHbaInfoHwVer_Object((1,3,6,1,4,1,9,9,373,1,2,1,1,7),_CfdmiHbaInfoHwVer_Type())
cfdmiHbaInfoHwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaInfoHwVer.setStatus(_A)
class _CfdmiHbaInfoDriverVer_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CfdmiHbaInfoDriverVer_Type.__name__=_D
_CfdmiHbaInfoDriverVer_Object=MibTableColumn
cfdmiHbaInfoDriverVer=_CfdmiHbaInfoDriverVer_Object((1,3,6,1,4,1,9,9,373,1,2,1,1,8),_CfdmiHbaInfoDriverVer_Type())
cfdmiHbaInfoDriverVer.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaInfoDriverVer.setStatus(_A)
class _CfdmiHbaInfoOptROMVer_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CfdmiHbaInfoOptROMVer_Type.__name__=_D
_CfdmiHbaInfoOptROMVer_Object=MibTableColumn
cfdmiHbaInfoOptROMVer=_CfdmiHbaInfoOptROMVer_Object((1,3,6,1,4,1,9,9,373,1,2,1,1,9),_CfdmiHbaInfoOptROMVer_Type())
cfdmiHbaInfoOptROMVer.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaInfoOptROMVer.setStatus(_A)
class _CfdmiHbaInfoFwVer_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CfdmiHbaInfoFwVer_Type.__name__=_D
_CfdmiHbaInfoFwVer_Object=MibTableColumn
cfdmiHbaInfoFwVer=_CfdmiHbaInfoFwVer_Object((1,3,6,1,4,1,9,9,373,1,2,1,1,10),_CfdmiHbaInfoFwVer_Type())
cfdmiHbaInfoFwVer.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaInfoFwVer.setStatus(_A)
class _CfdmiHbaInfoOSInfo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CfdmiHbaInfoOSInfo_Type.__name__=_D
_CfdmiHbaInfoOSInfo_Object=MibTableColumn
cfdmiHbaInfoOSInfo=_CfdmiHbaInfoOSInfo_Object((1,3,6,1,4,1,9,9,373,1,2,1,1,11),_CfdmiHbaInfoOSInfo_Type())
cfdmiHbaInfoOSInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaInfoOSInfo.setStatus(_A)
_CfdmiHbaInfoMaxCTPayload_Type=Unsigned32
_CfdmiHbaInfoMaxCTPayload_Object=MibTableColumn
cfdmiHbaInfoMaxCTPayload=_CfdmiHbaInfoMaxCTPayload_Object((1,3,6,1,4,1,9,9,373,1,2,1,1,12),_CfdmiHbaInfoMaxCTPayload_Type())
cfdmiHbaInfoMaxCTPayload.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaInfoMaxCTPayload.setStatus(_A)
if mibBuilder.loadTexts:cfdmiHbaInfoMaxCTPayload.setUnits('32-bit words')
_CfdmiHbaPortTable_Object=MibTable
cfdmiHbaPortTable=_CfdmiHbaPortTable_Object((1,3,6,1,4,1,9,9,373,1,2,2))
if mibBuilder.loadTexts:cfdmiHbaPortTable.setStatus(_A)
_CfdmiHbaPortEntry_Object=MibTableRow
cfdmiHbaPortEntry=_CfdmiHbaPortEntry_Object((1,3,6,1,4,1,9,9,373,1,2,2,1))
cfdmiHbaPortEntry.setIndexNames((0,_E,_G),(0,_B,_H),(0,_B,_Q))
if mibBuilder.loadTexts:cfdmiHbaPortEntry.setStatus(_A)
_CfdmiHbaPortId_Type=FcNameId
_CfdmiHbaPortId_Object=MibTableColumn
cfdmiHbaPortId=_CfdmiHbaPortId_Object((1,3,6,1,4,1,9,9,373,1,2,2,1,1),_CfdmiHbaPortId_Type())
cfdmiHbaPortId.setMaxAccess(_P)
if mibBuilder.loadTexts:cfdmiHbaPortId.setStatus(_A)
_CfdmiHbaPortSupportedFC4Type_Type=OctetString
_CfdmiHbaPortSupportedFC4Type_Object=MibTableColumn
cfdmiHbaPortSupportedFC4Type=_CfdmiHbaPortSupportedFC4Type_Object((1,3,6,1,4,1,9,9,373,1,2,2,1,2),_CfdmiHbaPortSupportedFC4Type_Type())
cfdmiHbaPortSupportedFC4Type.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaPortSupportedFC4Type.setStatus(_A)
_CfdmiHbaPortSupportedSpeed_Type=Unsigned32
_CfdmiHbaPortSupportedSpeed_Object=MibTableColumn
cfdmiHbaPortSupportedSpeed=_CfdmiHbaPortSupportedSpeed_Object((1,3,6,1,4,1,9,9,373,1,2,2,1,3),_CfdmiHbaPortSupportedSpeed_Type())
cfdmiHbaPortSupportedSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaPortSupportedSpeed.setStatus(_A)
_CfdmiHbaPortCurrentSpeed_Type=Unsigned32
_CfdmiHbaPortCurrentSpeed_Object=MibTableColumn
cfdmiHbaPortCurrentSpeed=_CfdmiHbaPortCurrentSpeed_Object((1,3,6,1,4,1,9,9,373,1,2,2,1,4),_CfdmiHbaPortCurrentSpeed_Type())
cfdmiHbaPortCurrentSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaPortCurrentSpeed.setStatus(_A)
_CfdmiHbaPortMaxFrameSize_Type=Unsigned32
_CfdmiHbaPortMaxFrameSize_Object=MibTableColumn
cfdmiHbaPortMaxFrameSize=_CfdmiHbaPortMaxFrameSize_Object((1,3,6,1,4,1,9,9,373,1,2,2,1,5),_CfdmiHbaPortMaxFrameSize_Type())
cfdmiHbaPortMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaPortMaxFrameSize.setStatus(_A)
class _CfdmiHbaPortOsDevName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CfdmiHbaPortOsDevName_Type.__name__=_D
_CfdmiHbaPortOsDevName_Object=MibTableColumn
cfdmiHbaPortOsDevName=_CfdmiHbaPortOsDevName_Object((1,3,6,1,4,1,9,9,373,1,2,2,1,6),_CfdmiHbaPortOsDevName_Type())
cfdmiHbaPortOsDevName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaPortOsDevName.setStatus(_A)
class _CfdmiHbaPortHostName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CfdmiHbaPortHostName_Type.__name__=_D
_CfdmiHbaPortHostName_Object=MibTableColumn
cfdmiHbaPortHostName=_CfdmiHbaPortHostName_Object((1,3,6,1,4,1,9,9,373,1,2,2,1,7),_CfdmiHbaPortHostName_Type())
cfdmiHbaPortHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:cfdmiHbaPortHostName.setStatus(_A)
_CfdmiRejectReasonCode_Type=CFdmiRejectReasonCode
_CfdmiRejectReasonCode_Object=MibScalar
cfdmiRejectReasonCode=_CfdmiRejectReasonCode_Object((1,3,6,1,4,1,9,9,373,1,2,3),_CfdmiRejectReasonCode_Type())
cfdmiRejectReasonCode.setMaxAccess(_F)
if mibBuilder.loadTexts:cfdmiRejectReasonCode.setStatus(_A)
_CfdmiRejectReasonCodeExpl_Type=CFdmiRejectReasonCodeExpl
_CfdmiRejectReasonCodeExpl_Object=MibScalar
cfdmiRejectReasonCodeExpl=_CfdmiRejectReasonCodeExpl_Object((1,3,6,1,4,1,9,9,373,1,2,4),_CfdmiRejectReasonCodeExpl_Type())
cfdmiRejectReasonCodeExpl.setMaxAccess(_F)
if mibBuilder.loadTexts:cfdmiRejectReasonCodeExpl.setStatus(_A)
class _CfdmiNotifyRegOperType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('regHBA',1),('regHAT',2),('regPRT',3),('regPA',4)))
_CfdmiNotifyRegOperType_Type.__name__=_N
_CfdmiNotifyRegOperType_Object=MibScalar
cfdmiNotifyRegOperType=_CfdmiNotifyRegOperType_Object((1,3,6,1,4,1,9,9,373,1,2,5),_CfdmiNotifyRegOperType_Type())
cfdmiNotifyRegOperType.setMaxAccess(_F)
if mibBuilder.loadTexts:cfdmiNotifyRegOperType.setStatus(_A)
_CfdmiNotifyHBAPortId_Type=FcNameId
_CfdmiNotifyHBAPortId_Object=MibScalar
cfdmiNotifyHBAPortId=_CfdmiNotifyHBAPortId_Object((1,3,6,1,4,1,9,9,373,1,2,6),_CfdmiNotifyHBAPortId_Type())
cfdmiNotifyHBAPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:cfdmiNotifyHBAPortId.setStatus(_A)
_CfdmiStatistics_ObjectIdentity=ObjectIdentity
cfdmiStatistics=_CfdmiStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,373,1,3))
_CiscoFdmiMIBConformance_ObjectIdentity=ObjectIdentity
ciscoFdmiMIBConformance=_CiscoFdmiMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,373,2))
_CiscoFdmiMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFdmiMIBCompliances=_CiscoFdmiMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,373,2,1))
_CiscoFdmiMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFdmiMIBGroups=_CiscoFdmiMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,373,2,2))
cfdmiConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,373,2,2,1))
cfdmiConfigGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:cfdmiConfigGroup.setStatus(_A)
cfdmiHbaInformationGroup=ObjectGroup((1,3,6,1,4,1,9,9,373,2,2,2))
cfdmiHbaInformationGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:cfdmiHbaInformationGroup.setStatus(_A)
cfdmiHbaPortInformationGroup=ObjectGroup((1,3,6,1,4,1,9,9,373,2,2,3))
cfdmiHbaPortInformationGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:cfdmiHbaPortInformationGroup.setStatus(_A)
cfdmiRejectRegNotify=NotificationType((1,3,6,1,4,1,9,9,373,0,1))
cfdmiRejectRegNotify.setObjects(*((_E,_M),(_B,_K),(_B,_L),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cfdmiRejectRegNotify.setStatus(_A)
cfdmiNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,373,2,2,4))
cfdmiNotificationGroup.setObjects((_B,_j))
if mibBuilder.loadTexts:cfdmiNotificationGroup.setStatus(_A)
ciscoFdmiMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,373,2,1,1))
ciscoFdmiMIBCompliance.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ciscoFdmiMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CFdmiRejectReasonCode':CFdmiRejectReasonCode,'CFdmiRejectReasonCodeExpl':CFdmiRejectReasonCodeExpl,'ciscoFdmiMIB':ciscoFdmiMIB,'ciscoFdmiMIBNotifications':ciscoFdmiMIBNotifications,_j:cfdmiRejectRegNotify,'ciscoFdmiMIBObjects':ciscoFdmiMIBObjects,'cfdmiConfig':cfdmiConfig,_R:cfdmiRejectRegNotifyEnable,'cfdmiInfo':cfdmiInfo,'cfdmiHbaInfoTable':cfdmiHbaInfoTable,'cfdmiHbaInfoEntry':cfdmiHbaInfoEntry,_H:cfdmiHbaInfoId,_S:cfdmiHbaInfoNodeName,_T:cfdmiHbaInfoMfg,_U:cfdmiHbaInfoSn,_V:cfdmiHbaInfoModel,_W:cfdmiHbaInfoModelDescr,_X:cfdmiHbaInfoHwVer,_Y:cfdmiHbaInfoDriverVer,_Z:cfdmiHbaInfoOptROMVer,_a:cfdmiHbaInfoFwVer,_b:cfdmiHbaInfoOSInfo,_c:cfdmiHbaInfoMaxCTPayload,'cfdmiHbaPortTable':cfdmiHbaPortTable,'cfdmiHbaPortEntry':cfdmiHbaPortEntry,_Q:cfdmiHbaPortId,_d:cfdmiHbaPortSupportedFC4Type,_e:cfdmiHbaPortSupportedSpeed,_f:cfdmiHbaPortCurrentSpeed,_g:cfdmiHbaPortMaxFrameSize,_h:cfdmiHbaPortOsDevName,_i:cfdmiHbaPortHostName,_I:cfdmiRejectReasonCode,_J:cfdmiRejectReasonCodeExpl,_K:cfdmiNotifyRegOperType,_L:cfdmiNotifyHBAPortId,'cfdmiStatistics':cfdmiStatistics,'ciscoFdmiMIBConformance':ciscoFdmiMIBConformance,'ciscoFdmiMIBCompliances':ciscoFdmiMIBCompliances,'ciscoFdmiMIBCompliance':ciscoFdmiMIBCompliance,'ciscoFdmiMIBGroups':ciscoFdmiMIBGroups,_k:cfdmiConfigGroup,_l:cfdmiHbaInformationGroup,_m:cfdmiHbaPortInformationGroup,_n:cfdmiNotificationGroup})