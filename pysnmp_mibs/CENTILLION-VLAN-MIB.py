_H='cnVlanPortMemberVID'
_G='cnVlanPortMemberPort'
_F='cnVlanPortMemberCard'
_E='Integer32'
_D='CENTILLION-VLAN-MIB'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanId,vlan=mibBuilder.importSymbols('CENTILLION-MCAST-MIB','VlanId','vlan')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
_CnVlanMemberGroup_ObjectIdentity=ObjectIdentity
cnVlanMemberGroup=_CnVlanMemberGroup_ObjectIdentity((1,3,6,1,4,1,930,2,1,2,31,2))
_CnVlanPortMemberTable_Object=MibTable
cnVlanPortMemberTable=_CnVlanPortMemberTable_Object((1,3,6,1,4,1,930,2,1,2,31,2,1))
if mibBuilder.loadTexts:cnVlanPortMemberTable.setStatus(_A)
_CnVlanPortMemberEntry_Object=MibTableRow
cnVlanPortMemberEntry=_CnVlanPortMemberEntry_Object((1,3,6,1,4,1,930,2,1,2,31,2,1,1))
cnVlanPortMemberEntry.setIndexNames((0,_D,_F),(0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:cnVlanPortMemberEntry.setStatus(_A)
_CnVlanPortMemberCard_Type=Integer32
_CnVlanPortMemberCard_Object=MibTableColumn
cnVlanPortMemberCard=_CnVlanPortMemberCard_Object((1,3,6,1,4,1,930,2,1,2,31,2,1,1,1),_CnVlanPortMemberCard_Type())
cnVlanPortMemberCard.setMaxAccess(_B)
if mibBuilder.loadTexts:cnVlanPortMemberCard.setStatus(_A)
_CnVlanPortMemberPort_Type=Integer32
_CnVlanPortMemberPort_Object=MibTableColumn
cnVlanPortMemberPort=_CnVlanPortMemberPort_Object((1,3,6,1,4,1,930,2,1,2,31,2,1,1,2),_CnVlanPortMemberPort_Type())
cnVlanPortMemberPort.setMaxAccess(_B)
if mibBuilder.loadTexts:cnVlanPortMemberPort.setStatus(_A)
_CnVlanPortMemberVID_Type=VlanId
_CnVlanPortMemberVID_Object=MibTableColumn
cnVlanPortMemberVID=_CnVlanPortMemberVID_Object((1,3,6,1,4,1,930,2,1,2,31,2,1,1,3),_CnVlanPortMemberVID_Type())
cnVlanPortMemberVID.setMaxAccess(_B)
if mibBuilder.loadTexts:cnVlanPortMemberVID.setStatus(_A)
_CnVlanPortMemberStatus_Type=RowStatus
_CnVlanPortMemberStatus_Object=MibTableColumn
cnVlanPortMemberStatus=_CnVlanPortMemberStatus_Object((1,3,6,1,4,1,930,2,1,2,31,2,1,1,4),_CnVlanPortMemberStatus_Type())
cnVlanPortMemberStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cnVlanPortMemberStatus.setStatus(_A)
class _CnVlanPortMemberIngressType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pvid',1),('tag',2),('protocolId',3)))
_CnVlanPortMemberIngressType_Type.__name__=_E
_CnVlanPortMemberIngressType_Object=MibTableColumn
cnVlanPortMemberIngressType=_CnVlanPortMemberIngressType_Object((1,3,6,1,4,1,930,2,1,2,31,2,1,1,5),_CnVlanPortMemberIngressType_Type())
cnVlanPortMemberIngressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnVlanPortMemberIngressType.setStatus(_A)
_CnVlanPortMemberDynamic_Type=TruthValue
_CnVlanPortMemberDynamic_Object=MibTableColumn
cnVlanPortMemberDynamic=_CnVlanPortMemberDynamic_Object((1,3,6,1,4,1,930,2,1,2,31,2,1,1,6),_CnVlanPortMemberDynamic_Type())
cnVlanPortMemberDynamic.setMaxAccess(_B)
if mibBuilder.loadTexts:cnVlanPortMemberDynamic.setStatus(_A)
_CnVlanPortMemberIfIndex_Type=InterfaceIndex
_CnVlanPortMemberIfIndex_Object=MibTableColumn
cnVlanPortMemberIfIndex=_CnVlanPortMemberIfIndex_Object((1,3,6,1,4,1,930,2,1,2,31,2,1,1,7),_CnVlanPortMemberIfIndex_Type())
cnVlanPortMemberIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cnVlanPortMemberIfIndex.setStatus(_A)
_CnVlanPortMemberRing_Type=Integer32
_CnVlanPortMemberRing_Object=MibTableColumn
cnVlanPortMemberRing=_CnVlanPortMemberRing_Object((1,3,6,1,4,1,930,2,1,2,31,2,1,1,8),_CnVlanPortMemberRing_Type())
cnVlanPortMemberRing.setMaxAccess(_C)
if mibBuilder.loadTexts:cnVlanPortMemberRing.setStatus(_A)
_CnVlanENETMgt_Type=VlanId
_CnVlanENETMgt_Object=MibScalar
cnVlanENETMgt=_CnVlanENETMgt_Object((1,3,6,1,4,1,930,2,1,2,31,3),_CnVlanENETMgt_Type())
cnVlanENETMgt.setMaxAccess(_C)
if mibBuilder.loadTexts:cnVlanENETMgt.setStatus(_A)
_CnVlanTRMgt_Type=VlanId
_CnVlanTRMgt_Object=MibScalar
cnVlanTRMgt=_CnVlanTRMgt_Object((1,3,6,1,4,1,930,2,1,2,31,4),_CnVlanTRMgt_Type())
cnVlanTRMgt.setMaxAccess(_C)
if mibBuilder.loadTexts:cnVlanTRMgt.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cnVlanMemberGroup':cnVlanMemberGroup,'cnVlanPortMemberTable':cnVlanPortMemberTable,'cnVlanPortMemberEntry':cnVlanPortMemberEntry,_F:cnVlanPortMemberCard,_G:cnVlanPortMemberPort,_H:cnVlanPortMemberVID,'cnVlanPortMemberStatus':cnVlanPortMemberStatus,'cnVlanPortMemberIngressType':cnVlanPortMemberIngressType,'cnVlanPortMemberDynamic':cnVlanPortMemberDynamic,'cnVlanPortMemberIfIndex':cnVlanPortMemberIfIndex,'cnVlanPortMemberRing':cnVlanPortMemberRing,'cnVlanENETMgt':cnVlanENETMgt,'cnVlanTRMgt':cnVlanTRMgt})