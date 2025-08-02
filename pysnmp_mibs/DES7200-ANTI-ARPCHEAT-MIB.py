_K='myAntiArpcheatMIBGroup'
_J='trustedArpOperationType'
_I='trustedArpVlan'
_H='trustedArpMediaPhysAddress'
_G='myTrustedArpDelete'
_F='read-create'
_E='trustedArpIp'
_D='trustedArpIfIndex'
_C='read-write'
_B='DES7200-ANTI-ARPCHEAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
IfIndex,=mibBuilder.importSymbols('DES7200-TC','IfIndex')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
myAntiArpcheatMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,41))
if mibBuilder.loadTexts:myAntiArpcheatMIB.setRevisions(('2007-01-29 00:00',))
_MyAntiArpcheatMIBObjects_ObjectIdentity=ObjectIdentity
myAntiArpcheatMIBObjects=_MyAntiArpcheatMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,41,1))
_MyTrustedArpDelete_Type=Integer32
_MyTrustedArpDelete_Object=MibScalar
myTrustedArpDelete=_MyTrustedArpDelete_Object((1,3,6,1,4,1,171,10,97,2,41,1,1),_MyTrustedArpDelete_Type())
myTrustedArpDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:myTrustedArpDelete.setStatus(_A)
_MyTrustedArpTable_Object=MibTable
myTrustedArpTable=_MyTrustedArpTable_Object((1,3,6,1,4,1,171,10,97,2,41,1,2))
if mibBuilder.loadTexts:myTrustedArpTable.setStatus(_A)
_MyTrustedArpEntry_Object=MibTableRow
myTrustedArpEntry=_MyTrustedArpEntry_Object((1,3,6,1,4,1,171,10,97,2,41,1,2,1))
myTrustedArpEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:myTrustedArpEntry.setStatus(_A)
_TrustedArpIfIndex_Type=IfIndex
_TrustedArpIfIndex_Object=MibTableColumn
trustedArpIfIndex=_TrustedArpIfIndex_Object((1,3,6,1,4,1,171,10,97,2,41,1,2,1,1),_TrustedArpIfIndex_Type())
trustedArpIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:trustedArpIfIndex.setStatus(_A)
_TrustedArpIp_Type=IpAddress
_TrustedArpIp_Object=MibTableColumn
trustedArpIp=_TrustedArpIp_Object((1,3,6,1,4,1,171,10,97,2,41,1,2,1,2),_TrustedArpIp_Type())
trustedArpIp.setMaxAccess(_F)
if mibBuilder.loadTexts:trustedArpIp.setStatus(_A)
_TrustedArpMediaPhysAddress_Type=MacAddress
_TrustedArpMediaPhysAddress_Object=MibTableColumn
trustedArpMediaPhysAddress=_TrustedArpMediaPhysAddress_Object((1,3,6,1,4,1,171,10,97,2,41,1,2,1,3),_TrustedArpMediaPhysAddress_Type())
trustedArpMediaPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trustedArpMediaPhysAddress.setStatus(_A)
_TrustedArpVlan_Type=VlanId
_TrustedArpVlan_Object=MibTableColumn
trustedArpVlan=_TrustedArpVlan_Object((1,3,6,1,4,1,171,10,97,2,41,1,2,1,4),_TrustedArpVlan_Type())
trustedArpVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:trustedArpVlan.setStatus(_A)
_TrustedArpOperationType_Type=Integer32
_TrustedArpOperationType_Object=MibTableColumn
trustedArpOperationType=_TrustedArpOperationType_Object((1,3,6,1,4,1,171,10,97,2,41,1,2,1,5),_TrustedArpOperationType_Type())
trustedArpOperationType.setMaxAccess(_C)
if mibBuilder.loadTexts:trustedArpOperationType.setStatus(_A)
_MyAntiArpcheatMIBConformance_ObjectIdentity=ObjectIdentity
myAntiArpcheatMIBConformance=_MyAntiArpcheatMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,41,2))
_MyAntiArpcheatMIBCompliances_ObjectIdentity=ObjectIdentity
myAntiArpcheatMIBCompliances=_MyAntiArpcheatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,41,2,1))
_MyAntiArpcheatMIBGroups_ObjectIdentity=ObjectIdentity
myAntiArpcheatMIBGroups=_MyAntiArpcheatMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,41,2,2))
myAntiArpcheatMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,41,2,2,1))
myAntiArpcheatMIBGroup.setObjects(*((_B,_G),(_B,_D),(_B,_E),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:myAntiArpcheatMIBGroup.setStatus(_A)
myAntiArpcheatMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,41,2,1,1))
myAntiArpcheatMIBCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:myAntiArpcheatMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myAntiArpcheatMIB':myAntiArpcheatMIB,'myAntiArpcheatMIBObjects':myAntiArpcheatMIBObjects,_G:myTrustedArpDelete,'myTrustedArpTable':myTrustedArpTable,'myTrustedArpEntry':myTrustedArpEntry,_D:trustedArpIfIndex,_E:trustedArpIp,_H:trustedArpMediaPhysAddress,_I:trustedArpVlan,_J:trustedArpOperationType,'myAntiArpcheatMIBConformance':myAntiArpcheatMIBConformance,'myAntiArpcheatMIBCompliances':myAntiArpcheatMIBCompliances,'myAntiArpcheatMIBCompliance':myAntiArpcheatMIBCompliance,'myAntiArpcheatMIBGroups':myAntiArpcheatMIBGroups,_K:myAntiArpcheatMIBGroup})