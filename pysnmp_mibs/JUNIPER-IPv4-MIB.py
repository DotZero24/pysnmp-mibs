_G='not-accessible'
_F='jnxIpv4AdEntAddr'
_E='jnxIpv4AdEntIfIndex'
_D='read-only'
_C='JUNIPER-IPv4-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
jnxIpv4=ModuleIdentity((1,3,6,1,4,1,2636,3,12))
if mibBuilder.loadTexts:jnxIpv4.setRevisions(('2001-08-31 00:00',))
_JnxIpv4Config_ObjectIdentity=ObjectIdentity
jnxIpv4Config=_JnxIpv4Config_ObjectIdentity((1,3,6,1,4,1,2636,3,12,1))
_JnxIpv4AddrTable_Object=MibTable
jnxIpv4AddrTable=_JnxIpv4AddrTable_Object((1,3,6,1,4,1,2636,3,12,1,1))
if mibBuilder.loadTexts:jnxIpv4AddrTable.setStatus(_A)
_JnxIpv4AddrEntry_Object=MibTableRow
jnxIpv4AddrEntry=_JnxIpv4AddrEntry_Object((1,3,6,1,4,1,2636,3,12,1,1,1))
jnxIpv4AddrEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:jnxIpv4AddrEntry.setStatus(_A)
class _JnxIpv4AdEntIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JnxIpv4AdEntIfIndex_Type.__name__=_B
_JnxIpv4AdEntIfIndex_Object=MibTableColumn
jnxIpv4AdEntIfIndex=_JnxIpv4AdEntIfIndex_Object((1,3,6,1,4,1,2636,3,12,1,1,1,1),_JnxIpv4AdEntIfIndex_Type())
jnxIpv4AdEntIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:jnxIpv4AdEntIfIndex.setStatus(_A)
_JnxIpv4AdEntAddr_Type=IpAddress
_JnxIpv4AdEntAddr_Object=MibTableColumn
jnxIpv4AdEntAddr=_JnxIpv4AdEntAddr_Object((1,3,6,1,4,1,2636,3,12,1,1,1,2),_JnxIpv4AdEntAddr_Type())
jnxIpv4AdEntAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:jnxIpv4AdEntAddr.setStatus(_A)
_JnxIpv4AdEntNetMask_Type=IpAddress
_JnxIpv4AdEntNetMask_Object=MibTableColumn
jnxIpv4AdEntNetMask=_JnxIpv4AdEntNetMask_Object((1,3,6,1,4,1,2636,3,12,1,1,1,3),_JnxIpv4AdEntNetMask_Type())
jnxIpv4AdEntNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxIpv4AdEntNetMask.setStatus(_A)
class _JnxIpv4AdEntBcastAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_JnxIpv4AdEntBcastAddr_Type.__name__=_B
_JnxIpv4AdEntBcastAddr_Object=MibTableColumn
jnxIpv4AdEntBcastAddr=_JnxIpv4AdEntBcastAddr_Object((1,3,6,1,4,1,2636,3,12,1,1,1,4),_JnxIpv4AdEntBcastAddr_Type())
jnxIpv4AdEntBcastAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxIpv4AdEntBcastAddr.setStatus(_A)
class _JnxIpv4AdEntReasmMaxSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_JnxIpv4AdEntReasmMaxSize_Type.__name__=_B
_JnxIpv4AdEntReasmMaxSize_Object=MibTableColumn
jnxIpv4AdEntReasmMaxSize=_JnxIpv4AdEntReasmMaxSize_Object((1,3,6,1,4,1,2636,3,12,1,1,1,5),_JnxIpv4AdEntReasmMaxSize_Type())
jnxIpv4AdEntReasmMaxSize.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxIpv4AdEntReasmMaxSize.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'jnxIpv4':jnxIpv4,'jnxIpv4Config':jnxIpv4Config,'jnxIpv4AddrTable':jnxIpv4AddrTable,'jnxIpv4AddrEntry':jnxIpv4AddrEntry,_E:jnxIpv4AdEntIfIndex,_F:jnxIpv4AdEntAddr,'jnxIpv4AdEntNetMask':jnxIpv4AdEntNetMask,'jnxIpv4AdEntBcastAddr':jnxIpv4AdEntBcastAddr,'jnxIpv4AdEntReasmMaxSize':jnxIpv4AdEntReasmMaxSize})