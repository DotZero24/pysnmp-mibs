_J='qtechAntiArpcheatMIBGroup'
_I='trustedArpOperationType'
_H='trustedArpVlan'
_G='trustedArpMediaPhysAddress'
_F='qtechTrustedArpDelete'
_E='trustedArpIp'
_D='trustedArpIfIndex'
_C='read-write'
_B='QTECH-ANTI-ARPCHEAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
IfIndex,=mibBuilder.importSymbols('QTECH-TC','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
qtechAntiArpcheatMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,41))
if mibBuilder.loadTexts:qtechAntiArpcheatMIB.setRevisions(('2007-01-29 00:00',))
_QtechAntiArpcheatMIBObjects_ObjectIdentity=ObjectIdentity
qtechAntiArpcheatMIBObjects=_QtechAntiArpcheatMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,41,1))
_QtechTrustedArpDelete_Type=Integer32
_QtechTrustedArpDelete_Object=MibScalar
qtechTrustedArpDelete=_QtechTrustedArpDelete_Object((1,3,6,1,4,1,27514,1,1,10,2,41,1,1),_QtechTrustedArpDelete_Type())
qtechTrustedArpDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTrustedArpDelete.setStatus(_A)
_QtechTrustedArpTable_Object=MibTable
qtechTrustedArpTable=_QtechTrustedArpTable_Object((1,3,6,1,4,1,27514,1,1,10,2,41,1,2))
if mibBuilder.loadTexts:qtechTrustedArpTable.setStatus(_A)
_QtechTrustedArpEntry_Object=MibTableRow
qtechTrustedArpEntry=_QtechTrustedArpEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,41,1,2,1))
qtechTrustedArpEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:qtechTrustedArpEntry.setStatus(_A)
_TrustedArpIfIndex_Type=IfIndex
_TrustedArpIfIndex_Object=MibTableColumn
trustedArpIfIndex=_TrustedArpIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,41,1,2,1,1),_TrustedArpIfIndex_Type())
trustedArpIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:trustedArpIfIndex.setStatus(_A)
_TrustedArpIp_Type=IpAddress
_TrustedArpIp_Object=MibTableColumn
trustedArpIp=_TrustedArpIp_Object((1,3,6,1,4,1,27514,1,1,10,2,41,1,2,1,2),_TrustedArpIp_Type())
trustedArpIp.setMaxAccess(_C)
if mibBuilder.loadTexts:trustedArpIp.setStatus(_A)
_TrustedArpMediaPhysAddress_Type=MacAddress
_TrustedArpMediaPhysAddress_Object=MibTableColumn
trustedArpMediaPhysAddress=_TrustedArpMediaPhysAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,41,1,2,1,3),_TrustedArpMediaPhysAddress_Type())
trustedArpMediaPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trustedArpMediaPhysAddress.setStatus(_A)
_TrustedArpVlan_Type=VlanId
_TrustedArpVlan_Object=MibTableColumn
trustedArpVlan=_TrustedArpVlan_Object((1,3,6,1,4,1,27514,1,1,10,2,41,1,2,1,4),_TrustedArpVlan_Type())
trustedArpVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:trustedArpVlan.setStatus(_A)
_TrustedArpOperationType_Type=Integer32
_TrustedArpOperationType_Object=MibTableColumn
trustedArpOperationType=_TrustedArpOperationType_Object((1,3,6,1,4,1,27514,1,1,10,2,41,1,2,1,5),_TrustedArpOperationType_Type())
trustedArpOperationType.setMaxAccess(_C)
if mibBuilder.loadTexts:trustedArpOperationType.setStatus(_A)
_QtechAntiArpcheatMIBConformance_ObjectIdentity=ObjectIdentity
qtechAntiArpcheatMIBConformance=_QtechAntiArpcheatMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,41,2))
_QtechAntiArpcheatMIBCompliances_ObjectIdentity=ObjectIdentity
qtechAntiArpcheatMIBCompliances=_QtechAntiArpcheatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,41,2,1))
_QtechAntiArpcheatMIBGroups_ObjectIdentity=ObjectIdentity
qtechAntiArpcheatMIBGroups=_QtechAntiArpcheatMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,41,2,2))
qtechAntiArpcheatMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,41,2,2,1))
qtechAntiArpcheatMIBGroup.setObjects(*((_B,_F),(_B,_D),(_B,_E),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:qtechAntiArpcheatMIBGroup.setStatus(_A)
qtechAntiArpcheatMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,41,2,1,1))
qtechAntiArpcheatMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:qtechAntiArpcheatMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechAntiArpcheatMIB':qtechAntiArpcheatMIB,'qtechAntiArpcheatMIBObjects':qtechAntiArpcheatMIBObjects,_F:qtechTrustedArpDelete,'qtechTrustedArpTable':qtechTrustedArpTable,'qtechTrustedArpEntry':qtechTrustedArpEntry,_D:trustedArpIfIndex,_E:trustedArpIp,_G:trustedArpMediaPhysAddress,_H:trustedArpVlan,_I:trustedArpOperationType,'qtechAntiArpcheatMIBConformance':qtechAntiArpcheatMIBConformance,'qtechAntiArpcheatMIBCompliances':qtechAntiArpcheatMIBCompliances,'qtechAntiArpcheatMIBCompliance':qtechAntiArpcheatMIBCompliance,'qtechAntiArpcheatMIBGroups':qtechAntiArpcheatMIBGroups,_J:qtechAntiArpcheatMIBGroup})