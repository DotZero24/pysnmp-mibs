_O='h3cDnsDynamicSrvIpGroup'
_N='h3cDnsStaticSrvIpGroup'
_M='h3cDnsDynamicSrvIpPriority'
_L='h3cDnsStaticSrvIpRowStatus'
_K='h3cDnsStaticSrvIpPriority'
_J='h3cDnsDynamicSrvIpAddr'
_I='h3cDnsDynamicSrvIpType'
_H='read-only'
_G='h3cDnsStaticSrvIpAddr'
_F='h3cDnsStaticSrvIpType'
_E='Integer32'
_D='InetAddress'
_C='not-accessible'
_B='A3COM-HUAWEI-DNS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_D,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cDns=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,97))
if mibBuilder.loadTexts:h3cDns.setRevisions(('2009-02-12 00:00',))
_H3cDnsObjects_ObjectIdentity=ObjectIdentity
h3cDnsObjects=_H3cDnsObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,97,1))
_H3cDnsStaticSrvIpTable_Object=MibTable
h3cDnsStaticSrvIpTable=_H3cDnsStaticSrvIpTable_Object((1,3,6,1,4,1,43,45,1,10,2,97,1,1))
if mibBuilder.loadTexts:h3cDnsStaticSrvIpTable.setStatus(_A)
_H3cDnsStaticSrvIpEntry_Object=MibTableRow
h3cDnsStaticSrvIpEntry=_H3cDnsStaticSrvIpEntry_Object((1,3,6,1,4,1,43,45,1,10,2,97,1,1,1))
h3cDnsStaticSrvIpEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:h3cDnsStaticSrvIpEntry.setStatus(_A)
_H3cDnsStaticSrvIpType_Type=InetAddressType
_H3cDnsStaticSrvIpType_Object=MibTableColumn
h3cDnsStaticSrvIpType=_H3cDnsStaticSrvIpType_Object((1,3,6,1,4,1,43,45,1,10,2,97,1,1,1,1),_H3cDnsStaticSrvIpType_Type())
h3cDnsStaticSrvIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDnsStaticSrvIpType.setStatus(_A)
class _H3cDnsStaticSrvIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cDnsStaticSrvIpAddr_Type.__name__=_D
_H3cDnsStaticSrvIpAddr_Object=MibTableColumn
h3cDnsStaticSrvIpAddr=_H3cDnsStaticSrvIpAddr_Object((1,3,6,1,4,1,43,45,1,10,2,97,1,1,1,2),_H3cDnsStaticSrvIpAddr_Type())
h3cDnsStaticSrvIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDnsStaticSrvIpAddr.setStatus(_A)
class _H3cDnsStaticSrvIpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cDnsStaticSrvIpPriority_Type.__name__=_E
_H3cDnsStaticSrvIpPriority_Object=MibTableColumn
h3cDnsStaticSrvIpPriority=_H3cDnsStaticSrvIpPriority_Object((1,3,6,1,4,1,43,45,1,10,2,97,1,1,1,3),_H3cDnsStaticSrvIpPriority_Type())
h3cDnsStaticSrvIpPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDnsStaticSrvIpPriority.setStatus(_A)
_H3cDnsStaticSrvIpRowStatus_Type=RowStatus
_H3cDnsStaticSrvIpRowStatus_Object=MibTableColumn
h3cDnsStaticSrvIpRowStatus=_H3cDnsStaticSrvIpRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,97,1,1,1,4),_H3cDnsStaticSrvIpRowStatus_Type())
h3cDnsStaticSrvIpRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:h3cDnsStaticSrvIpRowStatus.setStatus(_A)
_H3cDnsDynamicSrvIpTable_Object=MibTable
h3cDnsDynamicSrvIpTable=_H3cDnsDynamicSrvIpTable_Object((1,3,6,1,4,1,43,45,1,10,2,97,1,2))
if mibBuilder.loadTexts:h3cDnsDynamicSrvIpTable.setStatus(_A)
_H3cDnsDynamicSrvIpEntry_Object=MibTableRow
h3cDnsDynamicSrvIpEntry=_H3cDnsDynamicSrvIpEntry_Object((1,3,6,1,4,1,43,45,1,10,2,97,1,2,1))
h3cDnsDynamicSrvIpEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:h3cDnsDynamicSrvIpEntry.setStatus(_A)
_H3cDnsDynamicSrvIpType_Type=InetAddressType
_H3cDnsDynamicSrvIpType_Object=MibTableColumn
h3cDnsDynamicSrvIpType=_H3cDnsDynamicSrvIpType_Object((1,3,6,1,4,1,43,45,1,10,2,97,1,2,1,1),_H3cDnsDynamicSrvIpType_Type())
h3cDnsDynamicSrvIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDnsDynamicSrvIpType.setStatus(_A)
class _H3cDnsDynamicSrvIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cDnsDynamicSrvIpAddr_Type.__name__=_D
_H3cDnsDynamicSrvIpAddr_Object=MibTableColumn
h3cDnsDynamicSrvIpAddr=_H3cDnsDynamicSrvIpAddr_Object((1,3,6,1,4,1,43,45,1,10,2,97,1,2,1,2),_H3cDnsDynamicSrvIpAddr_Type())
h3cDnsDynamicSrvIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDnsDynamicSrvIpAddr.setStatus(_A)
class _H3cDnsDynamicSrvIpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cDnsDynamicSrvIpPriority_Type.__name__=_E
_H3cDnsDynamicSrvIpPriority_Object=MibTableColumn
h3cDnsDynamicSrvIpPriority=_H3cDnsDynamicSrvIpPriority_Object((1,3,6,1,4,1,43,45,1,10,2,97,1,2,1,3),_H3cDnsDynamicSrvIpPriority_Type())
h3cDnsDynamicSrvIpPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDnsDynamicSrvIpPriority.setStatus(_A)
_H3cDnsMIBConformance_ObjectIdentity=ObjectIdentity
h3cDnsMIBConformance=_H3cDnsMIBConformance_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,97,2))
_H3cDnsMIBCompliances_ObjectIdentity=ObjectIdentity
h3cDnsMIBCompliances=_H3cDnsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,97,2,1))
_H3cDnsMIBGroups_ObjectIdentity=ObjectIdentity
h3cDnsMIBGroups=_H3cDnsMIBGroups_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,97,2,2))
h3cDnsStaticSrvIpGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,97,2,2,1))
h3cDnsStaticSrvIpGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:h3cDnsStaticSrvIpGroup.setStatus(_A)
h3cDnsDynamicSrvIpGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,97,2,2,2))
h3cDnsDynamicSrvIpGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:h3cDnsDynamicSrvIpGroup.setStatus(_A)
h3cDnsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,43,45,1,10,2,97,2,1,1))
h3cDnsMIBCompliance.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:h3cDnsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cDns':h3cDns,'h3cDnsObjects':h3cDnsObjects,'h3cDnsStaticSrvIpTable':h3cDnsStaticSrvIpTable,'h3cDnsStaticSrvIpEntry':h3cDnsStaticSrvIpEntry,_F:h3cDnsStaticSrvIpType,_G:h3cDnsStaticSrvIpAddr,_K:h3cDnsStaticSrvIpPriority,_L:h3cDnsStaticSrvIpRowStatus,'h3cDnsDynamicSrvIpTable':h3cDnsDynamicSrvIpTable,'h3cDnsDynamicSrvIpEntry':h3cDnsDynamicSrvIpEntry,_I:h3cDnsDynamicSrvIpType,_J:h3cDnsDynamicSrvIpAddr,_M:h3cDnsDynamicSrvIpPriority,'h3cDnsMIBConformance':h3cDnsMIBConformance,'h3cDnsMIBCompliances':h3cDnsMIBCompliances,'h3cDnsMIBCompliance':h3cDnsMIBCompliance,'h3cDnsMIBGroups':h3cDnsMIBGroups,_N:h3cDnsStaticSrvIpGroup,_O:h3cDnsDynamicSrvIpGroup})