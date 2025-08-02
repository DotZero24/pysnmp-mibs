_O='hpnicfDnsDynamicSrvIpGroup'
_N='hpnicfDnsStaticSrvIpGroup'
_M='hpnicfDnsDynamicSrvIpPriority'
_L='hpnicfDnsStaticSrvIpRowStatus'
_K='hpnicfDnsStaticSrvIpPriority'
_J='hpnicfDnsDynamicSrvIpAddr'
_I='hpnicfDnsDynamicSrvIpType'
_H='read-only'
_G='hpnicfDnsStaticSrvIpAddr'
_F='hpnicfDnsStaticSrvIpType'
_E='Integer32'
_D='InetAddress'
_C='not-accessible'
_B='HPN-ICF-DNS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_D,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfDns=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,97))
if mibBuilder.loadTexts:hpnicfDns.setRevisions(('2009-02-12 00:00',))
_HpnicfDnsObjects_ObjectIdentity=ObjectIdentity
hpnicfDnsObjects=_HpnicfDnsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,97,1))
_HpnicfDnsStaticSrvIpTable_Object=MibTable
hpnicfDnsStaticSrvIpTable=_HpnicfDnsStaticSrvIpTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,97,1,1))
if mibBuilder.loadTexts:hpnicfDnsStaticSrvIpTable.setStatus(_A)
_HpnicfDnsStaticSrvIpEntry_Object=MibTableRow
hpnicfDnsStaticSrvIpEntry=_HpnicfDnsStaticSrvIpEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,97,1,1,1))
hpnicfDnsStaticSrvIpEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfDnsStaticSrvIpEntry.setStatus(_A)
_HpnicfDnsStaticSrvIpType_Type=InetAddressType
_HpnicfDnsStaticSrvIpType_Object=MibTableColumn
hpnicfDnsStaticSrvIpType=_HpnicfDnsStaticSrvIpType_Object((1,3,6,1,4,1,11,2,14,11,15,2,97,1,1,1,1),_HpnicfDnsStaticSrvIpType_Type())
hpnicfDnsStaticSrvIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDnsStaticSrvIpType.setStatus(_A)
class _HpnicfDnsStaticSrvIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfDnsStaticSrvIpAddr_Type.__name__=_D
_HpnicfDnsStaticSrvIpAddr_Object=MibTableColumn
hpnicfDnsStaticSrvIpAddr=_HpnicfDnsStaticSrvIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,97,1,1,1,2),_HpnicfDnsStaticSrvIpAddr_Type())
hpnicfDnsStaticSrvIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDnsStaticSrvIpAddr.setStatus(_A)
class _HpnicfDnsStaticSrvIpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfDnsStaticSrvIpPriority_Type.__name__=_E
_HpnicfDnsStaticSrvIpPriority_Object=MibTableColumn
hpnicfDnsStaticSrvIpPriority=_HpnicfDnsStaticSrvIpPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,97,1,1,1,3),_HpnicfDnsStaticSrvIpPriority_Type())
hpnicfDnsStaticSrvIpPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDnsStaticSrvIpPriority.setStatus(_A)
_HpnicfDnsStaticSrvIpRowStatus_Type=RowStatus
_HpnicfDnsStaticSrvIpRowStatus_Object=MibTableColumn
hpnicfDnsStaticSrvIpRowStatus=_HpnicfDnsStaticSrvIpRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,97,1,1,1,4),_HpnicfDnsStaticSrvIpRowStatus_Type())
hpnicfDnsStaticSrvIpRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpnicfDnsStaticSrvIpRowStatus.setStatus(_A)
_HpnicfDnsDynamicSrvIpTable_Object=MibTable
hpnicfDnsDynamicSrvIpTable=_HpnicfDnsDynamicSrvIpTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,97,1,2))
if mibBuilder.loadTexts:hpnicfDnsDynamicSrvIpTable.setStatus(_A)
_HpnicfDnsDynamicSrvIpEntry_Object=MibTableRow
hpnicfDnsDynamicSrvIpEntry=_HpnicfDnsDynamicSrvIpEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,97,1,2,1))
hpnicfDnsDynamicSrvIpEntry.setIndexNames((0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:hpnicfDnsDynamicSrvIpEntry.setStatus(_A)
_HpnicfDnsDynamicSrvIpType_Type=InetAddressType
_HpnicfDnsDynamicSrvIpType_Object=MibTableColumn
hpnicfDnsDynamicSrvIpType=_HpnicfDnsDynamicSrvIpType_Object((1,3,6,1,4,1,11,2,14,11,15,2,97,1,2,1,1),_HpnicfDnsDynamicSrvIpType_Type())
hpnicfDnsDynamicSrvIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDnsDynamicSrvIpType.setStatus(_A)
class _HpnicfDnsDynamicSrvIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfDnsDynamicSrvIpAddr_Type.__name__=_D
_HpnicfDnsDynamicSrvIpAddr_Object=MibTableColumn
hpnicfDnsDynamicSrvIpAddr=_HpnicfDnsDynamicSrvIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,97,1,2,1,2),_HpnicfDnsDynamicSrvIpAddr_Type())
hpnicfDnsDynamicSrvIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDnsDynamicSrvIpAddr.setStatus(_A)
class _HpnicfDnsDynamicSrvIpPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfDnsDynamicSrvIpPriority_Type.__name__=_E
_HpnicfDnsDynamicSrvIpPriority_Object=MibTableColumn
hpnicfDnsDynamicSrvIpPriority=_HpnicfDnsDynamicSrvIpPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,97,1,2,1,3),_HpnicfDnsDynamicSrvIpPriority_Type())
hpnicfDnsDynamicSrvIpPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDnsDynamicSrvIpPriority.setStatus(_A)
_HpnicfDnsMIBConformance_ObjectIdentity=ObjectIdentity
hpnicfDnsMIBConformance=_HpnicfDnsMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,97,2))
_HpnicfDnsMIBCompliances_ObjectIdentity=ObjectIdentity
hpnicfDnsMIBCompliances=_HpnicfDnsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,97,2,1))
_HpnicfDnsMIBGroups_ObjectIdentity=ObjectIdentity
hpnicfDnsMIBGroups=_HpnicfDnsMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,97,2,2))
hpnicfDnsStaticSrvIpGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,97,2,2,1))
hpnicfDnsStaticSrvIpGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:hpnicfDnsStaticSrvIpGroup.setStatus(_A)
hpnicfDnsDynamicSrvIpGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,97,2,2,2))
hpnicfDnsDynamicSrvIpGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:hpnicfDnsDynamicSrvIpGroup.setStatus(_A)
hpnicfDnsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,97,2,1,1))
hpnicfDnsMIBCompliance.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:hpnicfDnsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfDns':hpnicfDns,'hpnicfDnsObjects':hpnicfDnsObjects,'hpnicfDnsStaticSrvIpTable':hpnicfDnsStaticSrvIpTable,'hpnicfDnsStaticSrvIpEntry':hpnicfDnsStaticSrvIpEntry,_F:hpnicfDnsStaticSrvIpType,_G:hpnicfDnsStaticSrvIpAddr,_K:hpnicfDnsStaticSrvIpPriority,_L:hpnicfDnsStaticSrvIpRowStatus,'hpnicfDnsDynamicSrvIpTable':hpnicfDnsDynamicSrvIpTable,'hpnicfDnsDynamicSrvIpEntry':hpnicfDnsDynamicSrvIpEntry,_I:hpnicfDnsDynamicSrvIpType,_J:hpnicfDnsDynamicSrvIpAddr,_M:hpnicfDnsDynamicSrvIpPriority,'hpnicfDnsMIBConformance':hpnicfDnsMIBConformance,'hpnicfDnsMIBCompliances':hpnicfDnsMIBCompliances,'hpnicfDnsMIBCompliance':hpnicfDnsMIBCompliance,'hpnicfDnsMIBGroups':hpnicfDnsMIBGroups,_N:hpnicfDnsStaticSrvIpGroup,_O:hpnicfDnsDynamicSrvIpGroup})