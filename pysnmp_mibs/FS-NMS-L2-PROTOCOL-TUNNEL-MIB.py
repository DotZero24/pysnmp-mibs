_D='Integer32'
_C='ifIndex'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmsMgmt,=mibBuilder.importSymbols('FS-NMS-SMI','nmsMgmt')
ifIndex,=mibBuilder.importSymbols(_B,_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nmsL2ProtocolTunnelMIB=ModuleIdentity((1,3,6,1,4,1,52642,9,357))
_L2ptMIBObjects_ObjectIdentity=ObjectIdentity
l2ptMIBObjects=_L2ptMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,9,357,1))
_L2ptGlobal_ObjectIdentity=ObjectIdentity
l2ptGlobal=_L2ptGlobal_ObjectIdentity((1,3,6,1,4,1,52642,9,357,1,1))
_L2ptIntfTable_Object=MibTable
l2ptIntfTable=_L2ptIntfTable_Object((1,3,6,1,4,1,52642,9,357,1,2))
if mibBuilder.loadTexts:l2ptIntfTable.setStatus(_A)
_L2ptIntfEntry_Object=MibTableRow
l2ptIntfEntry=_L2ptIntfEntry_Object((1,3,6,1,4,1,52642,9,357,1,2,1))
l2ptIntfEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:l2ptIntfEntry.setStatus(_A)
class _L2ptIntfStpTnl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_L2ptIntfStpTnl_Type.__name__=_D
_L2ptIntfStpTnl_Object=MibTableColumn
l2ptIntfStpTnl=_L2ptIntfStpTnl_Object((1,3,6,1,4,1,52642,9,357,1,2,1,1),_L2ptIntfStpTnl_Type())
l2ptIntfStpTnl.setMaxAccess('read-write')
if mibBuilder.loadTexts:l2ptIntfStpTnl.setStatus(_A)
mibBuilder.exportSymbols('FS-NMS-L2-PROTOCOL-TUNNEL-MIB',**{'nmsL2ProtocolTunnelMIB':nmsL2ProtocolTunnelMIB,'l2ptMIBObjects':l2ptMIBObjects,'l2ptGlobal':l2ptGlobal,'l2ptIntfTable':l2ptIntfTable,'l2ptIntfEntry':l2ptIntfEntry,'l2ptIntfStpTnl':l2ptIntfStpTnl})