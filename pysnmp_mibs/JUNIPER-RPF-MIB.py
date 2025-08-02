_G='read-only'
_F='not-accessible'
_E='jnxRpfStatsAddrFamily'
_D='jnxRpfStatsIfIndex'
_C='Integer32'
_B='JUNIPER-RPF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
jnxRpf=ModuleIdentity((1,3,6,1,4,1,2636,3,17))
if mibBuilder.loadTexts:jnxRpf.setRevisions(('2002-02-25 00:00',))
_JnxRpfStats_ObjectIdentity=ObjectIdentity
jnxRpfStats=_JnxRpfStats_ObjectIdentity((1,3,6,1,4,1,2636,3,17,1))
_JnxRpfStatsTable_Object=MibTable
jnxRpfStatsTable=_JnxRpfStatsTable_Object((1,3,6,1,4,1,2636,3,17,1,1))
if mibBuilder.loadTexts:jnxRpfStatsTable.setStatus(_A)
_JnxRpfStatsEntry_Object=MibTableRow
jnxRpfStatsEntry=_JnxRpfStatsEntry_Object((1,3,6,1,4,1,2636,3,17,1,1,1))
jnxRpfStatsEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:jnxRpfStatsEntry.setStatus(_A)
_JnxRpfStatsIfIndex_Type=InterfaceIndex
_JnxRpfStatsIfIndex_Object=MibTableColumn
jnxRpfStatsIfIndex=_JnxRpfStatsIfIndex_Object((1,3,6,1,4,1,2636,3,17,1,1,1,1),_JnxRpfStatsIfIndex_Type())
jnxRpfStatsIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxRpfStatsIfIndex.setStatus(_A)
class _JnxRpfStatsAddrFamily_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_JnxRpfStatsAddrFamily_Type.__name__=_C
_JnxRpfStatsAddrFamily_Object=MibTableColumn
jnxRpfStatsAddrFamily=_JnxRpfStatsAddrFamily_Object((1,3,6,1,4,1,2636,3,17,1,1,1,2),_JnxRpfStatsAddrFamily_Type())
jnxRpfStatsAddrFamily.setMaxAccess(_F)
if mibBuilder.loadTexts:jnxRpfStatsAddrFamily.setStatus(_A)
_JnxRpfStatsPackets_Type=Counter64
_JnxRpfStatsPackets_Object=MibTableColumn
jnxRpfStatsPackets=_JnxRpfStatsPackets_Object((1,3,6,1,4,1,2636,3,17,1,1,1,3),_JnxRpfStatsPackets_Type())
jnxRpfStatsPackets.setMaxAccess(_G)
if mibBuilder.loadTexts:jnxRpfStatsPackets.setStatus(_A)
_JnxRpfStatsBytes_Type=Counter64
_JnxRpfStatsBytes_Object=MibTableColumn
jnxRpfStatsBytes=_JnxRpfStatsBytes_Object((1,3,6,1,4,1,2636,3,17,1,1,1,4),_JnxRpfStatsBytes_Type())
jnxRpfStatsBytes.setMaxAccess(_G)
if mibBuilder.loadTexts:jnxRpfStatsBytes.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'jnxRpf':jnxRpf,'jnxRpfStats':jnxRpfStats,'jnxRpfStatsTable':jnxRpfStatsTable,'jnxRpfStatsEntry':jnxRpfStatsEntry,_D:jnxRpfStatsIfIndex,_E:jnxRpfStatsAddrFamily,'jnxRpfStatsPackets':jnxRpfStatsPackets,'jnxRpfStatsBytes':jnxRpfStatsBytes})