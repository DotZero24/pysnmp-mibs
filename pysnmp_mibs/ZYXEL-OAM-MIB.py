_D='read-write'
_C='ifIndex'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_B,_C)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelOam=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,56))
_ZyxelOamSetup_ObjectIdentity=ObjectIdentity
zyxelOamSetup=_ZyxelOamSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,56,1))
_ZyOamState_Type=EnabledStatus
_ZyOamState_Object=MibScalar
zyOamState=_ZyOamState_Object((1,3,6,1,4,1,890,1,15,3,56,1,1),_ZyOamState_Type())
zyOamState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOamState.setStatus(_A)
_ZyxelOamPortTable_Object=MibTable
zyxelOamPortTable=_ZyxelOamPortTable_Object((1,3,6,1,4,1,890,1,15,3,56,1,2))
if mibBuilder.loadTexts:zyxelOamPortTable.setStatus(_A)
_ZyxelOamPortEntry_Object=MibTableRow
zyxelOamPortEntry=_ZyxelOamPortEntry_Object((1,3,6,1,4,1,890,1,15,3,56,1,2,1))
zyxelOamPortEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:zyxelOamPortEntry.setStatus(_A)
class _ZyOamPortFunctionsSupported_Type(Bits):namedValues=NamedValues(*(('unidirectionalSupport',0),('loopbackSupport',1),('eventSupport',2),('variableSupport',3)))
_ZyOamPortFunctionsSupported_Type.__name__='Bits'
_ZyOamPortFunctionsSupported_Object=MibTableColumn
zyOamPortFunctionsSupported=_ZyOamPortFunctionsSupported_Object((1,3,6,1,4,1,890,1,15,3,56,1,2,1,1),_ZyOamPortFunctionsSupported_Type())
zyOamPortFunctionsSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:zyOamPortFunctionsSupported.setStatus(_A)
mibBuilder.exportSymbols('ZYXEL-OAM-MIB',**{'zyxelOam':zyxelOam,'zyxelOamSetup':zyxelOamSetup,'zyOamState':zyOamState,'zyxelOamPortTable':zyxelOamPortTable,'zyxelOamPortEntry':zyxelOamPortEntry,'zyOamPortFunctionsSupported':zyOamPortFunctionsSupported})