_J='fsAntiArpcheatMIBGroup'
_I='trustedArpOperationType'
_H='trustedArpVlan'
_G='trustedArpMediaPhysAddress'
_F='fsTrustedArpDelete'
_E='trustedArpIp'
_D='trustedArpIfIndex'
_C='read-write'
_B='FS-ANTI-ARPCHEAT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
fsAntiArpcheatMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,41))
if mibBuilder.loadTexts:fsAntiArpcheatMIB.setRevisions(('2007-01-29 00:00',))
_FsAntiArpcheatMIBObjects_ObjectIdentity=ObjectIdentity
fsAntiArpcheatMIBObjects=_FsAntiArpcheatMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,41,1))
_FsTrustedArpDelete_Type=Integer32
_FsTrustedArpDelete_Object=MibScalar
fsTrustedArpDelete=_FsTrustedArpDelete_Object((1,3,6,1,4,1,52642,1,1,10,2,41,1,1),_FsTrustedArpDelete_Type())
fsTrustedArpDelete.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTrustedArpDelete.setStatus(_A)
_FsTrustedArpTable_Object=MibTable
fsTrustedArpTable=_FsTrustedArpTable_Object((1,3,6,1,4,1,52642,1,1,10,2,41,1,2))
if mibBuilder.loadTexts:fsTrustedArpTable.setStatus(_A)
_FsTrustedArpEntry_Object=MibTableRow
fsTrustedArpEntry=_FsTrustedArpEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,41,1,2,1))
fsTrustedArpEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:fsTrustedArpEntry.setStatus(_A)
_TrustedArpIfIndex_Type=IfIndex
_TrustedArpIfIndex_Object=MibTableColumn
trustedArpIfIndex=_TrustedArpIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,41,1,2,1,1),_TrustedArpIfIndex_Type())
trustedArpIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:trustedArpIfIndex.setStatus(_A)
_TrustedArpIp_Type=IpAddress
_TrustedArpIp_Object=MibTableColumn
trustedArpIp=_TrustedArpIp_Object((1,3,6,1,4,1,52642,1,1,10,2,41,1,2,1,2),_TrustedArpIp_Type())
trustedArpIp.setMaxAccess(_C)
if mibBuilder.loadTexts:trustedArpIp.setStatus(_A)
_TrustedArpMediaPhysAddress_Type=MacAddress
_TrustedArpMediaPhysAddress_Object=MibTableColumn
trustedArpMediaPhysAddress=_TrustedArpMediaPhysAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,41,1,2,1,3),_TrustedArpMediaPhysAddress_Type())
trustedArpMediaPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trustedArpMediaPhysAddress.setStatus(_A)
_TrustedArpVlan_Type=VlanId
_TrustedArpVlan_Object=MibTableColumn
trustedArpVlan=_TrustedArpVlan_Object((1,3,6,1,4,1,52642,1,1,10,2,41,1,2,1,4),_TrustedArpVlan_Type())
trustedArpVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:trustedArpVlan.setStatus(_A)
_TrustedArpOperationType_Type=Integer32
_TrustedArpOperationType_Object=MibTableColumn
trustedArpOperationType=_TrustedArpOperationType_Object((1,3,6,1,4,1,52642,1,1,10,2,41,1,2,1,5),_TrustedArpOperationType_Type())
trustedArpOperationType.setMaxAccess(_C)
if mibBuilder.loadTexts:trustedArpOperationType.setStatus(_A)
_FsAntiArpcheatMIBConformance_ObjectIdentity=ObjectIdentity
fsAntiArpcheatMIBConformance=_FsAntiArpcheatMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,41,2))
_FsAntiArpcheatMIBCompliances_ObjectIdentity=ObjectIdentity
fsAntiArpcheatMIBCompliances=_FsAntiArpcheatMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,41,2,1))
_FsAntiArpcheatMIBGroups_ObjectIdentity=ObjectIdentity
fsAntiArpcheatMIBGroups=_FsAntiArpcheatMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,41,2,2))
fsAntiArpcheatMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,41,2,2,1))
fsAntiArpcheatMIBGroup.setObjects(*((_B,_F),(_B,_D),(_B,_E),(_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:fsAntiArpcheatMIBGroup.setStatus(_A)
fsAntiArpcheatMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,41,2,1,1))
fsAntiArpcheatMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:fsAntiArpcheatMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsAntiArpcheatMIB':fsAntiArpcheatMIB,'fsAntiArpcheatMIBObjects':fsAntiArpcheatMIBObjects,_F:fsTrustedArpDelete,'fsTrustedArpTable':fsTrustedArpTable,'fsTrustedArpEntry':fsTrustedArpEntry,_D:trustedArpIfIndex,_E:trustedArpIp,_G:trustedArpMediaPhysAddress,_H:trustedArpVlan,_I:trustedArpOperationType,'fsAntiArpcheatMIBConformance':fsAntiArpcheatMIBConformance,'fsAntiArpcheatMIBCompliances':fsAntiArpcheatMIBCompliances,'fsAntiArpcheatMIBCompliance':fsAntiArpcheatMIBCompliance,'fsAntiArpcheatMIBGroups':fsAntiArpcheatMIBGroups,_J:fsAntiArpcheatMIBGroup})