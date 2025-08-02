_I='jnxScuStatsClassName'
_H='jnxScuStatsAddrFamily'
_G='jnxScuStatsDstIfIndex'
_F='Integer32'
_E='read-only'
_D='not-accessible'
_C='SnmpAdminString'
_B='JUNIPER-SCU-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
jnxScu=ModuleIdentity((1,3,6,1,4,1,2636,3,16))
if mibBuilder.loadTexts:jnxScu.setRevisions(('2002-02-25 00:00',))
_JnxScuStats_ObjectIdentity=ObjectIdentity
jnxScuStats=_JnxScuStats_ObjectIdentity((1,3,6,1,4,1,2636,3,16,1))
_JnxScuStatsTable_Object=MibTable
jnxScuStatsTable=_JnxScuStatsTable_Object((1,3,6,1,4,1,2636,3,16,1,1))
if mibBuilder.loadTexts:jnxScuStatsTable.setStatus(_A)
_JnxScuStatsEntry_Object=MibTableRow
jnxScuStatsEntry=_JnxScuStatsEntry_Object((1,3,6,1,4,1,2636,3,16,1,1,1))
jnxScuStatsEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:jnxScuStatsEntry.setStatus(_A)
_JnxScuStatsDstIfIndex_Type=InterfaceIndex
_JnxScuStatsDstIfIndex_Object=MibTableColumn
jnxScuStatsDstIfIndex=_JnxScuStatsDstIfIndex_Object((1,3,6,1,4,1,2636,3,16,1,1,1,1),_JnxScuStatsDstIfIndex_Type())
jnxScuStatsDstIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxScuStatsDstIfIndex.setStatus(_A)
class _JnxScuStatsAddrFamily_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv4',1),('ipv6',2)))
_JnxScuStatsAddrFamily_Type.__name__=_F
_JnxScuStatsAddrFamily_Object=MibTableColumn
jnxScuStatsAddrFamily=_JnxScuStatsAddrFamily_Object((1,3,6,1,4,1,2636,3,16,1,1,1,2),_JnxScuStatsAddrFamily_Type())
jnxScuStatsAddrFamily.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxScuStatsAddrFamily.setStatus(_A)
class _JnxScuStatsClassName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,112))
_JnxScuStatsClassName_Type.__name__=_C
_JnxScuStatsClassName_Object=MibTableColumn
jnxScuStatsClassName=_JnxScuStatsClassName_Object((1,3,6,1,4,1,2636,3,16,1,1,1,3),_JnxScuStatsClassName_Type())
jnxScuStatsClassName.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxScuStatsClassName.setStatus(_A)
_JnxScuStatsPackets_Type=Counter64
_JnxScuStatsPackets_Object=MibTableColumn
jnxScuStatsPackets=_JnxScuStatsPackets_Object((1,3,6,1,4,1,2636,3,16,1,1,1,4),_JnxScuStatsPackets_Type())
jnxScuStatsPackets.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxScuStatsPackets.setStatus(_A)
_JnxScuStatsBytes_Type=Counter64
_JnxScuStatsBytes_Object=MibTableColumn
jnxScuStatsBytes=_JnxScuStatsBytes_Object((1,3,6,1,4,1,2636,3,16,1,1,1,5),_JnxScuStatsBytes_Type())
jnxScuStatsBytes.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxScuStatsBytes.setStatus(_A)
class _JnxScuStatsClName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,112))
_JnxScuStatsClName_Type.__name__=_C
_JnxScuStatsClName_Object=MibTableColumn
jnxScuStatsClName=_JnxScuStatsClName_Object((1,3,6,1,4,1,2636,3,16,1,1,1,6),_JnxScuStatsClName_Type())
jnxScuStatsClName.setMaxAccess(_E)
if mibBuilder.loadTexts:jnxScuStatsClName.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'jnxScu':jnxScu,'jnxScuStats':jnxScuStats,'jnxScuStatsTable':jnxScuStatsTable,'jnxScuStatsEntry':jnxScuStatsEntry,_G:jnxScuStatsDstIfIndex,_H:jnxScuStatsAddrFamily,_I:jnxScuStatsClassName,'jnxScuStatsPackets':jnxScuStatsPackets,'jnxScuStatsBytes':jnxScuStatsBytes,'jnxScuStatsClName':jnxScuStatsClName})