_V='ciscoLanAdaptGroup'
_U='ciscoLanGroup'
_T='cipCardLanAdaptAdminRowStatus'
_S='cipCardLanAdaptAdminAdaptName'
_R='cipCardLanAdaptAdminMacAddress'
_Q='cipCardLanAdminRowStatus'
_P='cipCardLanAdminTbBridgeGrp'
_O='cipCardLanAdminSrbTargetRing'
_N='cipCardLanAdminSrbBridgeNum'
_M='cipCardLanAdminSrbLocalRing'
_L='cipCardLanAdminBridgeType'
_K='cipCardLanAdaptAdminAdaptNo'
_J='DisplayString'
_I='not-accessible'
_H='cipCardLanAdminLanId'
_G='cipCardLanAdminLanType'
_F='ifIndex'
_E='IF-MIB'
_D='read-create'
_C='Integer32'
_B='CISCO-CIPLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention')
ciscoCipLanMIB=ModuleIdentity((1,3,6,1,4,1,9,9,34))
if mibBuilder.loadTexts:ciscoCipLanMIB.setRevisions(('1998-01-06 00:00','1995-04-28 00:00'))
_CipLanObjects_ObjectIdentity=ObjectIdentity
cipLanObjects=_CipLanObjects_ObjectIdentity((1,3,6,1,4,1,9,9,34,1))
_CipLan_ObjectIdentity=ObjectIdentity
cipLan=_CipLan_ObjectIdentity((1,3,6,1,4,1,9,9,34,1,1))
_CipCardLanAdminTable_Object=MibTable
cipCardLanAdminTable=_CipCardLanAdminTable_Object((1,3,6,1,4,1,9,9,34,1,1,1))
if mibBuilder.loadTexts:cipCardLanAdminTable.setStatus(_A)
_CipCardLanAdminEntry_Object=MibTableRow
cipCardLanAdminEntry=_CipCardLanAdminEntry_Object((1,3,6,1,4,1,9,9,34,1,1,1,1))
cipCardLanAdminEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:cipCardLanAdminEntry.setStatus(_A)
class _CipCardLanAdminLanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('iso88023csmacd',1),('iso88025tokenRing',2),('fddi',3)))
_CipCardLanAdminLanType_Type.__name__=_C
_CipCardLanAdminLanType_Object=MibTableColumn
cipCardLanAdminLanType=_CipCardLanAdminLanType_Object((1,3,6,1,4,1,9,9,34,1,1,1,1,1),_CipCardLanAdminLanType_Type())
cipCardLanAdminLanType.setMaxAccess(_I)
if mibBuilder.loadTexts:cipCardLanAdminLanType.setStatus(_A)
class _CipCardLanAdminLanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_CipCardLanAdminLanId_Type.__name__=_C
_CipCardLanAdminLanId_Object=MibTableColumn
cipCardLanAdminLanId=_CipCardLanAdminLanId_Object((1,3,6,1,4,1,9,9,34,1,1,1,1,2),_CipCardLanAdminLanId_Type())
cipCardLanAdminLanId.setMaxAccess(_I)
if mibBuilder.loadTexts:cipCardLanAdminLanId.setStatus(_A)
class _CipCardLanAdminBridgeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('transparentOnly',1),('sourcerouteOnly',2),('transpAndSourceRoute',3)))
_CipCardLanAdminBridgeType_Type.__name__=_C
_CipCardLanAdminBridgeType_Object=MibTableColumn
cipCardLanAdminBridgeType=_CipCardLanAdminBridgeType_Object((1,3,6,1,4,1,9,9,34,1,1,1,1,3),_CipCardLanAdminBridgeType_Type())
cipCardLanAdminBridgeType.setMaxAccess(_D)
if mibBuilder.loadTexts:cipCardLanAdminBridgeType.setStatus(_A)
class _CipCardLanAdminSrbLocalRing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_CipCardLanAdminSrbLocalRing_Type.__name__=_C
_CipCardLanAdminSrbLocalRing_Object=MibTableColumn
cipCardLanAdminSrbLocalRing=_CipCardLanAdminSrbLocalRing_Object((1,3,6,1,4,1,9,9,34,1,1,1,1,4),_CipCardLanAdminSrbLocalRing_Type())
cipCardLanAdminSrbLocalRing.setMaxAccess(_D)
if mibBuilder.loadTexts:cipCardLanAdminSrbLocalRing.setStatus(_A)
class _CipCardLanAdminSrbBridgeNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CipCardLanAdminSrbBridgeNum_Type.__name__=_C
_CipCardLanAdminSrbBridgeNum_Object=MibTableColumn
cipCardLanAdminSrbBridgeNum=_CipCardLanAdminSrbBridgeNum_Object((1,3,6,1,4,1,9,9,34,1,1,1,1,5),_CipCardLanAdminSrbBridgeNum_Type())
cipCardLanAdminSrbBridgeNum.setMaxAccess(_D)
if mibBuilder.loadTexts:cipCardLanAdminSrbBridgeNum.setStatus(_A)
class _CipCardLanAdminSrbTargetRing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_CipCardLanAdminSrbTargetRing_Type.__name__=_C
_CipCardLanAdminSrbTargetRing_Object=MibTableColumn
cipCardLanAdminSrbTargetRing=_CipCardLanAdminSrbTargetRing_Object((1,3,6,1,4,1,9,9,34,1,1,1,1,6),_CipCardLanAdminSrbTargetRing_Type())
cipCardLanAdminSrbTargetRing.setMaxAccess(_D)
if mibBuilder.loadTexts:cipCardLanAdminSrbTargetRing.setStatus(_A)
class _CipCardLanAdminTbBridgeGrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_CipCardLanAdminTbBridgeGrp_Type.__name__=_C
_CipCardLanAdminTbBridgeGrp_Object=MibTableColumn
cipCardLanAdminTbBridgeGrp=_CipCardLanAdminTbBridgeGrp_Object((1,3,6,1,4,1,9,9,34,1,1,1,1,7),_CipCardLanAdminTbBridgeGrp_Type())
cipCardLanAdminTbBridgeGrp.setMaxAccess(_D)
if mibBuilder.loadTexts:cipCardLanAdminTbBridgeGrp.setStatus(_A)
_CipCardLanAdminRowStatus_Type=RowStatus
_CipCardLanAdminRowStatus_Object=MibTableColumn
cipCardLanAdminRowStatus=_CipCardLanAdminRowStatus_Object((1,3,6,1,4,1,9,9,34,1,1,1,1,8),_CipCardLanAdminRowStatus_Type())
cipCardLanAdminRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cipCardLanAdminRowStatus.setStatus(_A)
_CipCardLanAdaptAdminTable_Object=MibTable
cipCardLanAdaptAdminTable=_CipCardLanAdaptAdminTable_Object((1,3,6,1,4,1,9,9,34,1,1,2))
if mibBuilder.loadTexts:cipCardLanAdaptAdminTable.setStatus(_A)
_CipCardLanAdaptAdminEntry_Object=MibTableRow
cipCardLanAdaptAdminEntry=_CipCardLanAdaptAdminEntry_Object((1,3,6,1,4,1,9,9,34,1,1,2,1))
cipCardLanAdaptAdminEntry.setIndexNames((0,_E,_F),(0,_B,_G),(0,_B,_H),(0,_B,_K))
if mibBuilder.loadTexts:cipCardLanAdaptAdminEntry.setStatus(_A)
class _CipCardLanAdaptAdminAdaptNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_CipCardLanAdaptAdminAdaptNo_Type.__name__=_C
_CipCardLanAdaptAdminAdaptNo_Object=MibTableColumn
cipCardLanAdaptAdminAdaptNo=_CipCardLanAdaptAdminAdaptNo_Object((1,3,6,1,4,1,9,9,34,1,1,2,1,1),_CipCardLanAdaptAdminAdaptNo_Type())
cipCardLanAdaptAdminAdaptNo.setMaxAccess(_I)
if mibBuilder.loadTexts:cipCardLanAdaptAdminAdaptNo.setStatus(_A)
_CipCardLanAdaptAdminMacAddress_Type=MacAddress
_CipCardLanAdaptAdminMacAddress_Object=MibTableColumn
cipCardLanAdaptAdminMacAddress=_CipCardLanAdaptAdminMacAddress_Object((1,3,6,1,4,1,9,9,34,1,1,2,1,2),_CipCardLanAdaptAdminMacAddress_Type())
cipCardLanAdaptAdminMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cipCardLanAdaptAdminMacAddress.setStatus(_A)
class _CipCardLanAdaptAdminAdaptName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_CipCardLanAdaptAdminAdaptName_Type.__name__=_J
_CipCardLanAdaptAdminAdaptName_Object=MibTableColumn
cipCardLanAdaptAdminAdaptName=_CipCardLanAdaptAdminAdaptName_Object((1,3,6,1,4,1,9,9,34,1,1,2,1,3),_CipCardLanAdaptAdminAdaptName_Type())
cipCardLanAdaptAdminAdaptName.setMaxAccess(_D)
if mibBuilder.loadTexts:cipCardLanAdaptAdminAdaptName.setStatus(_A)
_CipCardLanAdaptAdminRowStatus_Type=RowStatus
_CipCardLanAdaptAdminRowStatus_Object=MibTableColumn
cipCardLanAdaptAdminRowStatus=_CipCardLanAdaptAdminRowStatus_Object((1,3,6,1,4,1,9,9,34,1,1,2,1,4),_CipCardLanAdaptAdminRowStatus_Type())
cipCardLanAdaptAdminRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cipCardLanAdaptAdminRowStatus.setStatus(_A)
_CiscoCipLanMibConformance_ObjectIdentity=ObjectIdentity
ciscoCipLanMibConformance=_CiscoCipLanMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,34,2))
_CiscoCipLanMibCompliances_ObjectIdentity=ObjectIdentity
ciscoCipLanMibCompliances=_CiscoCipLanMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,34,2,1))
_CiscoCipLanMibGroups_ObjectIdentity=ObjectIdentity
ciscoCipLanMibGroups=_CiscoCipLanMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,34,2,2))
ciscoLanGroup=ObjectGroup((1,3,6,1,4,1,9,9,34,2,2,1))
ciscoLanGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ciscoLanGroup.setStatus(_A)
ciscoLanAdaptGroup=ObjectGroup((1,3,6,1,4,1,9,9,34,2,2,2))
ciscoLanAdaptGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:ciscoLanAdaptGroup.setStatus(_A)
ciscoCipLanMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,34,2,1,1))
ciscoCipLanMibCompliance.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:ciscoCipLanMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCipLanMIB':ciscoCipLanMIB,'cipLanObjects':cipLanObjects,'cipLan':cipLan,'cipCardLanAdminTable':cipCardLanAdminTable,'cipCardLanAdminEntry':cipCardLanAdminEntry,_G:cipCardLanAdminLanType,_H:cipCardLanAdminLanId,_L:cipCardLanAdminBridgeType,_M:cipCardLanAdminSrbLocalRing,_N:cipCardLanAdminSrbBridgeNum,_O:cipCardLanAdminSrbTargetRing,_P:cipCardLanAdminTbBridgeGrp,_Q:cipCardLanAdminRowStatus,'cipCardLanAdaptAdminTable':cipCardLanAdaptAdminTable,'cipCardLanAdaptAdminEntry':cipCardLanAdaptAdminEntry,_K:cipCardLanAdaptAdminAdaptNo,_R:cipCardLanAdaptAdminMacAddress,_S:cipCardLanAdaptAdminAdaptName,_T:cipCardLanAdaptAdminRowStatus,'ciscoCipLanMibConformance':ciscoCipLanMibConformance,'ciscoCipLanMibCompliances':ciscoCipLanMibCompliances,'ciscoCipLanMibCompliance':ciscoCipLanMibCompliance,'ciscoCipLanMibGroups':ciscoCipLanMibGroups,_U:ciscoLanGroup,_V:ciscoLanAdaptGroup})