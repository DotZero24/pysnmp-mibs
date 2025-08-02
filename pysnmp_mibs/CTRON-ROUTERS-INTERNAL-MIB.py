_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Cabletron_ObjectIdentity=ObjectIdentity
cabletron=_Cabletron_ObjectIdentity((1,3,6,1,4,1,52))
_Mibs_ObjectIdentity=ObjectIdentity
mibs=_Mibs_ObjectIdentity((1,3,6,1,4,1,52,4))
_Ctron_ObjectIdentity=ObjectIdentity
ctron=_Ctron_ObjectIdentity((1,3,6,1,4,1,52,4,1))
_CtNetwork_ObjectIdentity=ObjectIdentity
ctNetwork=_CtNetwork_ObjectIdentity((1,3,6,1,4,1,52,4,1,3))
_CtronExp_ObjectIdentity=ObjectIdentity
ctronExp=_CtronExp_ObjectIdentity((1,3,6,1,4,1,52,4,2))
_CtronRouterExp_ObjectIdentity=ObjectIdentity
ctronRouterExp=_CtronRouterExp_ObjectIdentity((1,3,6,1,4,1,52,4,2,2))
_NwRouter_ObjectIdentity=ObjectIdentity
nwRouter=_NwRouter_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2))
_NwRtrTemp_ObjectIdentity=ObjectIdentity
nwRtrTemp=_NwRtrTemp_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,99))
_NwRtrTemp1_ObjectIdentity=ObjectIdentity
nwRtrTemp1=_NwRtrTemp1_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,99,2))
_NwRtrTemp2_ObjectIdentity=ObjectIdentity
nwRtrTemp2=_NwRtrTemp2_ObjectIdentity((1,3,6,1,4,1,52,4,2,2,2,99,2,2))
class _NwRtrSoftReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('reset',0))
_NwRtrSoftReset_Type.__name__=_A
_NwRtrSoftReset_Object=MibScalar
nwRtrSoftReset=_NwRtrSoftReset_Object((1,3,6,1,4,1,52,4,2,2,2,99,2,2,1),_NwRtrSoftReset_Type())
nwRtrSoftReset.setMaxAccess('read-write')
if mibBuilder.loadTexts:nwRtrSoftReset.setStatus('mandatory')
mibBuilder.exportSymbols('CTRON-ROUTERS-INTERNAL-MIB',**{'cabletron':cabletron,'mibs':mibs,'ctron':ctron,'ctNetwork':ctNetwork,'ctronExp':ctronExp,'ctronRouterExp':ctronRouterExp,'nwRouter':nwRouter,'nwRtrTemp':nwRtrTemp,'nwRtrTemp1':nwRtrTemp1,'nwRtrTemp2':nwRtrTemp2,'nwRtrSoftReset':nwRtrSoftReset})