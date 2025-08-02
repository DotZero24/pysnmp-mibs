_H='read-create'
_G='not-accessible'
_F='jnxTRCtlTestName'
_E='jnxTRCtlOwnerIndex'
_D='JUNIPER-TRACEROUTE-MIB'
_C='DisplayString'
_B='SnmpAdminString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_B)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
jnxTraceRouteMIB=ModuleIdentity((1,3,6,1,4,1,2636,3,8))
_JnxTraceRouteObjects_ObjectIdentity=ObjectIdentity
jnxTraceRouteObjects=_JnxTraceRouteObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,8,1))
_JnxTraceRouteCtlTable_Object=MibTable
jnxTraceRouteCtlTable=_JnxTraceRouteCtlTable_Object((1,3,6,1,4,1,2636,3,8,1,2))
if mibBuilder.loadTexts:jnxTraceRouteCtlTable.setStatus(_A)
_JnxTraceRouteCtlEntry_Object=MibTableRow
jnxTraceRouteCtlEntry=_JnxTraceRouteCtlEntry_Object((1,3,6,1,4,1,2636,3,8,1,2,1))
jnxTraceRouteCtlEntry.setIndexNames((0,_D,_E),(0,_D,_F))
if mibBuilder.loadTexts:jnxTraceRouteCtlEntry.setStatus(_A)
class _JnxTRCtlOwnerIndex_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JnxTRCtlOwnerIndex_Type.__name__=_B
_JnxTRCtlOwnerIndex_Object=MibTableColumn
jnxTRCtlOwnerIndex=_JnxTRCtlOwnerIndex_Object((1,3,6,1,4,1,2636,3,8,1,2,1,1),_JnxTRCtlOwnerIndex_Type())
jnxTRCtlOwnerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:jnxTRCtlOwnerIndex.setStatus(_A)
class _JnxTRCtlTestName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_JnxTRCtlTestName_Type.__name__=_B
_JnxTRCtlTestName_Object=MibTableColumn
jnxTRCtlTestName=_JnxTRCtlTestName_Object((1,3,6,1,4,1,2636,3,8,1,2,1,2),_JnxTRCtlTestName_Type())
jnxTRCtlTestName.setMaxAccess(_G)
if mibBuilder.loadTexts:jnxTRCtlTestName.setStatus(_A)
class _JnxTRCtlIfName_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_JnxTRCtlIfName_Type.__name__=_C
_JnxTRCtlIfName_Object=MibTableColumn
jnxTRCtlIfName=_JnxTRCtlIfName_Object((1,3,6,1,4,1,2636,3,8,1,2,1,3),_JnxTRCtlIfName_Type())
jnxTRCtlIfName.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxTRCtlIfName.setStatus(_A)
class _JnxTRCtlRoutingInstanceName_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_JnxTRCtlRoutingInstanceName_Type.__name__=_C
_JnxTRCtlRoutingInstanceName_Object=MibTableColumn
jnxTRCtlRoutingInstanceName=_JnxTRCtlRoutingInstanceName_Object((1,3,6,1,4,1,2636,3,8,1,2,1,4),_JnxTRCtlRoutingInstanceName_Type())
jnxTRCtlRoutingInstanceName.setMaxAccess(_H)
if mibBuilder.loadTexts:jnxTRCtlRoutingInstanceName.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'jnxTraceRouteMIB':jnxTraceRouteMIB,'jnxTraceRouteObjects':jnxTraceRouteObjects,'jnxTraceRouteCtlTable':jnxTraceRouteCtlTable,'jnxTraceRouteCtlEntry':jnxTraceRouteCtlEntry,_E:jnxTRCtlOwnerIndex,_F:jnxTRCtlTestName,'jnxTRCtlIfName':jnxTRCtlIfName,'jnxTRCtlRoutingInstanceName':jnxTRCtlRoutingInstanceName})