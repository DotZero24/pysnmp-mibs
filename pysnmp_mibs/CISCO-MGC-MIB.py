_m='cMgcGrpProtocolGroup'
_l='cMgcGrpGroup'
_k='cMgcGrpParamGroup'
_j='cMgcIpMIBGroup'
_i='cMgcMIBGroup'
_h='cMgcGrpProtocolRowStatus'
_g='cMgcGrpProtocolPreference'
_f='cMgcGrpRowStatus'
_e='cMgcGrpMgcUdpPort'
_d='cMgcGrpMgcPreference'
_c='cMgcGrpStateChangeNtfy'
_b='cMgcGrpNumProtocol'
_a='cMgcGrpAssociationInfo'
_Z='cMgcGrpNumMgc'
_Y='cMgcIpRowStatus'
_X='cMgcIpPreference'
_W='cMgcIpAddressType'
_V='cMgcIpAddress'
_U='cMgcResolution'
_T='cMgcNumIP'
_S='cMgcNumMgcGroups'
_R='cMgcDomainName'
_Q='cMgcIpIndex'
_P='read-write'
_O='TruthValue'
_N='SnmpAdminString'
_M='InetAddressType'
_L='CiscoPort'
_K='cmgwSignalProtocolIndex'
_J='not-accessible'
_I='cMgcGrpIndex'
_H='cMgcIndex'
_G='read-only'
_F='cmgwIndex'
_E='CISCO-MEDIA-GATEWAY-MIB'
_D='read-create'
_C='Integer32'
_B='CISCO-MGC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cmgwIndex,cmgwSignalProtocolIndex=mibBuilder.importSymbols(_E,_F,_K)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoPort,=mibBuilder.importSymbols('CISCO-TC',_L)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_M)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_N)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_O)
ciscoMgcMIB=ModuleIdentity((1,3,6,1,4,1,9,9,321))
if mibBuilder.loadTexts:ciscoMgcMIB.setRevisions(('2003-04-18 00:00',))
class CMgcGroupIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
class CMgcGroupIndexOrZero(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_CMgcMibNotifications_ObjectIdentity=ObjectIdentity
cMgcMibNotifications=_CMgcMibNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,321,0))
_CMgcMibObjects_ObjectIdentity=ObjectIdentity
cMgcMibObjects=_CMgcMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,321,1))
_CMgcConfig_ObjectIdentity=ObjectIdentity
cMgcConfig=_CMgcConfig_ObjectIdentity((1,3,6,1,4,1,9,9,321,1,1))
_CMgcConfigTable_Object=MibTable
cMgcConfigTable=_CMgcConfigTable_Object((1,3,6,1,4,1,9,9,321,1,1,1))
if mibBuilder.loadTexts:cMgcConfigTable.setStatus(_A)
_CMgcConfigEntry_Object=MibTableRow
cMgcConfigEntry=_CMgcConfigEntry_Object((1,3,6,1,4,1,9,9,321,1,1,1,1))
cMgcConfigEntry.setIndexNames((0,_E,_F),(0,_B,_H))
if mibBuilder.loadTexts:cMgcConfigEntry.setStatus(_A)
class _CMgcIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CMgcIndex_Type.__name__=_C
_CMgcIndex_Object=MibTableColumn
cMgcIndex=_CMgcIndex_Object((1,3,6,1,4,1,9,9,321,1,1,1,1,1),_CMgcIndex_Type())
cMgcIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cMgcIndex.setStatus(_A)
class _CMgcDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CMgcDomainName_Type.__name__=_N
_CMgcDomainName_Object=MibTableColumn
cMgcDomainName=_CMgcDomainName_Object((1,3,6,1,4,1,9,9,321,1,1,1,1,2),_CMgcDomainName_Type())
cMgcDomainName.setMaxAccess(_G)
if mibBuilder.loadTexts:cMgcDomainName.setStatus(_A)
class _CMgcNumMgcGroups_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CMgcNumMgcGroups_Type.__name__=_C
_CMgcNumMgcGroups_Object=MibTableColumn
cMgcNumMgcGroups=_CMgcNumMgcGroups_Object((1,3,6,1,4,1,9,9,321,1,1,1,1,3),_CMgcNumMgcGroups_Type())
cMgcNumMgcGroups.setMaxAccess(_G)
if mibBuilder.loadTexts:cMgcNumMgcGroups.setStatus(_A)
class _CMgcNumIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CMgcNumIP_Type.__name__=_C
_CMgcNumIP_Object=MibTableColumn
cMgcNumIP=_CMgcNumIP_Object((1,3,6,1,4,1,9,9,321,1,1,1,1,4),_CMgcNumIP_Type())
cMgcNumIP.setMaxAccess(_G)
if mibBuilder.loadTexts:cMgcNumIP.setStatus(_A)
class _CMgcResolution_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internalOnly',1),('externalOnly',2)))
_CMgcResolution_Type.__name__=_C
_CMgcResolution_Object=MibTableColumn
cMgcResolution=_CMgcResolution_Object((1,3,6,1,4,1,9,9,321,1,1,1,1,5),_CMgcResolution_Type())
cMgcResolution.setMaxAccess(_P)
if mibBuilder.loadTexts:cMgcResolution.setStatus(_A)
_CMgcIpConfigTable_Object=MibTable
cMgcIpConfigTable=_CMgcIpConfigTable_Object((1,3,6,1,4,1,9,9,321,1,1,2))
if mibBuilder.loadTexts:cMgcIpConfigTable.setStatus(_A)
_CMgcIpConfigEntry_Object=MibTableRow
cMgcIpConfigEntry=_CMgcIpConfigEntry_Object((1,3,6,1,4,1,9,9,321,1,1,2,1))
cMgcIpConfigEntry.setIndexNames((0,_E,_F),(0,_B,_H),(0,_B,_Q))
if mibBuilder.loadTexts:cMgcIpConfigEntry.setStatus(_A)
class _CMgcIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CMgcIpIndex_Type.__name__=_C
_CMgcIpIndex_Object=MibTableColumn
cMgcIpIndex=_CMgcIpIndex_Object((1,3,6,1,4,1,9,9,321,1,1,2,1,1),_CMgcIpIndex_Type())
cMgcIpIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cMgcIpIndex.setStatus(_A)
class _CMgcIpAddressType_Type(InetAddressType):defaultValue=1
_CMgcIpAddressType_Type.__name__=_M
_CMgcIpAddressType_Object=MibTableColumn
cMgcIpAddressType=_CMgcIpAddressType_Object((1,3,6,1,4,1,9,9,321,1,1,2,1,2),_CMgcIpAddressType_Type())
cMgcIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cMgcIpAddressType.setStatus(_A)
_CMgcIpAddress_Type=InetAddress
_CMgcIpAddress_Object=MibTableColumn
cMgcIpAddress=_CMgcIpAddress_Object((1,3,6,1,4,1,9,9,321,1,1,2,1,3),_CMgcIpAddress_Type())
cMgcIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cMgcIpAddress.setStatus(_A)
class _CMgcIpPreference_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CMgcIpPreference_Type.__name__=_C
_CMgcIpPreference_Object=MibTableColumn
cMgcIpPreference=_CMgcIpPreference_Object((1,3,6,1,4,1,9,9,321,1,1,2,1,4),_CMgcIpPreference_Type())
cMgcIpPreference.setMaxAccess(_D)
if mibBuilder.loadTexts:cMgcIpPreference.setStatus(_A)
_CMgcIpRowStatus_Type=RowStatus
_CMgcIpRowStatus_Object=MibTableColumn
cMgcIpRowStatus=_CMgcIpRowStatus_Object((1,3,6,1,4,1,9,9,321,1,1,2,1,5),_CMgcIpRowStatus_Type())
cMgcIpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cMgcIpRowStatus.setStatus(_A)
_CMgcGroupConfig_ObjectIdentity=ObjectIdentity
cMgcGroupConfig=_CMgcGroupConfig_ObjectIdentity((1,3,6,1,4,1,9,9,321,1,2))
_CMgcGrpParamTable_Object=MibTable
cMgcGrpParamTable=_CMgcGrpParamTable_Object((1,3,6,1,4,1,9,9,321,1,2,1))
if mibBuilder.loadTexts:cMgcGrpParamTable.setStatus(_A)
_CMgcGrpParamEntry_Object=MibTableRow
cMgcGrpParamEntry=_CMgcGrpParamEntry_Object((1,3,6,1,4,1,9,9,321,1,2,1,1))
cMgcGrpParamEntry.setIndexNames((0,_E,_F),(0,_B,_I))
if mibBuilder.loadTexts:cMgcGrpParamEntry.setStatus(_A)
_CMgcGrpIndex_Type=CMgcGroupIndex
_CMgcGrpIndex_Object=MibTableColumn
cMgcGrpIndex=_CMgcGrpIndex_Object((1,3,6,1,4,1,9,9,321,1,2,1,1,1),_CMgcGrpIndex_Type())
cMgcGrpIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:cMgcGrpIndex.setStatus(_A)
class _CMgcGrpNumMgc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_CMgcGrpNumMgc_Type.__name__=_C
_CMgcGrpNumMgc_Object=MibTableColumn
cMgcGrpNumMgc=_CMgcGrpNumMgc_Object((1,3,6,1,4,1,9,9,321,1,2,1,1,2),_CMgcGrpNumMgc_Type())
cMgcGrpNumMgc.setMaxAccess(_G)
if mibBuilder.loadTexts:cMgcGrpNumMgc.setStatus(_A)
_CMgcGrpAssociationInfo_Type=Unsigned32
_CMgcGrpAssociationInfo_Object=MibTableColumn
cMgcGrpAssociationInfo=_CMgcGrpAssociationInfo_Object((1,3,6,1,4,1,9,9,321,1,2,1,1,3),_CMgcGrpAssociationInfo_Type())
cMgcGrpAssociationInfo.setMaxAccess(_G)
if mibBuilder.loadTexts:cMgcGrpAssociationInfo.setStatus(_A)
class _CMgcGrpNumProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_CMgcGrpNumProtocol_Type.__name__=_C
_CMgcGrpNumProtocol_Object=MibTableColumn
cMgcGrpNumProtocol=_CMgcGrpNumProtocol_Object((1,3,6,1,4,1,9,9,321,1,2,1,1,4),_CMgcGrpNumProtocol_Type())
cMgcGrpNumProtocol.setMaxAccess(_G)
if mibBuilder.loadTexts:cMgcGrpNumProtocol.setStatus(_A)
class _CMgcGrpStateChangeNtfy_Type(TruthValue):defaultValue=1
_CMgcGrpStateChangeNtfy_Type.__name__=_O
_CMgcGrpStateChangeNtfy_Object=MibTableColumn
cMgcGrpStateChangeNtfy=_CMgcGrpStateChangeNtfy_Object((1,3,6,1,4,1,9,9,321,1,2,1,1,5),_CMgcGrpStateChangeNtfy_Type())
cMgcGrpStateChangeNtfy.setMaxAccess(_P)
if mibBuilder.loadTexts:cMgcGrpStateChangeNtfy.setStatus(_A)
_CMgcGrpTable_Object=MibTable
cMgcGrpTable=_CMgcGrpTable_Object((1,3,6,1,4,1,9,9,321,1,2,2))
if mibBuilder.loadTexts:cMgcGrpTable.setStatus(_A)
_CMgcGrpEntry_Object=MibTableRow
cMgcGrpEntry=_CMgcGrpEntry_Object((1,3,6,1,4,1,9,9,321,1,2,2,1))
cMgcGrpEntry.setIndexNames((0,_E,_F),(0,_B,_I),(0,_B,_H))
if mibBuilder.loadTexts:cMgcGrpEntry.setStatus(_A)
class _CMgcGrpMgcPreference_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_CMgcGrpMgcPreference_Type.__name__=_C
_CMgcGrpMgcPreference_Object=MibTableColumn
cMgcGrpMgcPreference=_CMgcGrpMgcPreference_Object((1,3,6,1,4,1,9,9,321,1,2,2,1,1),_CMgcGrpMgcPreference_Type())
cMgcGrpMgcPreference.setMaxAccess(_D)
if mibBuilder.loadTexts:cMgcGrpMgcPreference.setStatus(_A)
class _CMgcGrpMgcUdpPort_Type(CiscoPort):defaultValue=0
_CMgcGrpMgcUdpPort_Type.__name__=_L
_CMgcGrpMgcUdpPort_Object=MibTableColumn
cMgcGrpMgcUdpPort=_CMgcGrpMgcUdpPort_Object((1,3,6,1,4,1,9,9,321,1,2,2,1,2),_CMgcGrpMgcUdpPort_Type())
cMgcGrpMgcUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cMgcGrpMgcUdpPort.setStatus(_A)
_CMgcGrpRowStatus_Type=RowStatus
_CMgcGrpRowStatus_Object=MibTableColumn
cMgcGrpRowStatus=_CMgcGrpRowStatus_Object((1,3,6,1,4,1,9,9,321,1,2,2,1,3),_CMgcGrpRowStatus_Type())
cMgcGrpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cMgcGrpRowStatus.setStatus(_A)
_CMgcGrpProtocolTable_Object=MibTable
cMgcGrpProtocolTable=_CMgcGrpProtocolTable_Object((1,3,6,1,4,1,9,9,321,1,2,3))
if mibBuilder.loadTexts:cMgcGrpProtocolTable.setStatus(_A)
_CMgcGrpProtocolEntry_Object=MibTableRow
cMgcGrpProtocolEntry=_CMgcGrpProtocolEntry_Object((1,3,6,1,4,1,9,9,321,1,2,3,1))
cMgcGrpProtocolEntry.setIndexNames((0,_E,_F),(0,_B,_I),(0,_E,_K))
if mibBuilder.loadTexts:cMgcGrpProtocolEntry.setStatus(_A)
class _CMgcGrpProtocolPreference_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_CMgcGrpProtocolPreference_Type.__name__=_C
_CMgcGrpProtocolPreference_Object=MibTableColumn
cMgcGrpProtocolPreference=_CMgcGrpProtocolPreference_Object((1,3,6,1,4,1,9,9,321,1,2,3,1,1),_CMgcGrpProtocolPreference_Type())
cMgcGrpProtocolPreference.setMaxAccess(_D)
if mibBuilder.loadTexts:cMgcGrpProtocolPreference.setStatus(_A)
_CMgcGrpProtocolRowStatus_Type=RowStatus
_CMgcGrpProtocolRowStatus_Object=MibTableColumn
cMgcGrpProtocolRowStatus=_CMgcGrpProtocolRowStatus_Object((1,3,6,1,4,1,9,9,321,1,2,3,1,2),_CMgcGrpProtocolRowStatus_Type())
cMgcGrpProtocolRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cMgcGrpProtocolRowStatus.setStatus(_A)
_CMgcMIBConformance_ObjectIdentity=ObjectIdentity
cMgcMIBConformance=_CMgcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,321,2))
_CMgcMIBCompliances_ObjectIdentity=ObjectIdentity
cMgcMIBCompliances=_CMgcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,321,2,1))
_CMgcMIBGroups_ObjectIdentity=ObjectIdentity
cMgcMIBGroups=_CMgcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,321,2,2))
cMgcMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,321,2,2,1))
cMgcMIBGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:cMgcMIBGroup.setStatus(_A)
cMgcIpMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,321,2,2,2))
cMgcIpMIBGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:cMgcIpMIBGroup.setStatus(_A)
cMgcGrpParamGroup=ObjectGroup((1,3,6,1,4,1,9,9,321,2,2,3))
cMgcGrpParamGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:cMgcGrpParamGroup.setStatus(_A)
cMgcGrpGroup=ObjectGroup((1,3,6,1,4,1,9,9,321,2,2,4))
cMgcGrpGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:cMgcGrpGroup.setStatus(_A)
cMgcGrpProtocolGroup=ObjectGroup((1,3,6,1,4,1,9,9,321,2,2,5))
cMgcGrpProtocolGroup.setObjects(*((_B,_g),(_B,_h)))
if mibBuilder.loadTexts:cMgcGrpProtocolGroup.setStatus(_A)
cMgcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,321,2,1,1))
cMgcMIBCompliance.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:cMgcMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CMgcGroupIndex':CMgcGroupIndex,'CMgcGroupIndexOrZero':CMgcGroupIndexOrZero,'ciscoMgcMIB':ciscoMgcMIB,'cMgcMibNotifications':cMgcMibNotifications,'cMgcMibObjects':cMgcMibObjects,'cMgcConfig':cMgcConfig,'cMgcConfigTable':cMgcConfigTable,'cMgcConfigEntry':cMgcConfigEntry,_H:cMgcIndex,_R:cMgcDomainName,_S:cMgcNumMgcGroups,_T:cMgcNumIP,_U:cMgcResolution,'cMgcIpConfigTable':cMgcIpConfigTable,'cMgcIpConfigEntry':cMgcIpConfigEntry,_Q:cMgcIpIndex,_W:cMgcIpAddressType,_V:cMgcIpAddress,_X:cMgcIpPreference,_Y:cMgcIpRowStatus,'cMgcGroupConfig':cMgcGroupConfig,'cMgcGrpParamTable':cMgcGrpParamTable,'cMgcGrpParamEntry':cMgcGrpParamEntry,_I:cMgcGrpIndex,_Z:cMgcGrpNumMgc,_a:cMgcGrpAssociationInfo,_b:cMgcGrpNumProtocol,_c:cMgcGrpStateChangeNtfy,'cMgcGrpTable':cMgcGrpTable,'cMgcGrpEntry':cMgcGrpEntry,_d:cMgcGrpMgcPreference,_e:cMgcGrpMgcUdpPort,_f:cMgcGrpRowStatus,'cMgcGrpProtocolTable':cMgcGrpProtocolTable,'cMgcGrpProtocolEntry':cMgcGrpProtocolEntry,_g:cMgcGrpProtocolPreference,_h:cMgcGrpProtocolRowStatus,'cMgcMIBConformance':cMgcMIBConformance,'cMgcMIBCompliances':cMgcMIBCompliances,'cMgcMIBCompliance':cMgcMIBCompliance,'cMgcMIBGroups':cMgcMIBGroups,_i:cMgcMIBGroup,_j:cMgcIpMIBGroup,_k:cMgcGrpParamGroup,_l:cMgcGrpGroup,_m:cMgcGrpProtocolGroup})