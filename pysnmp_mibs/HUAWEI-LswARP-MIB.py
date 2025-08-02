_D='hwLswIfIndex'
_C='HUAWEI-LswARP-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lswCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','lswCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwLswArpMib=ModuleIdentity((1,3,6,1,4,1,2011,2,23,1,4))
if mibBuilder.loadTexts:hwLswArpMib.setRevisions(('2001-06-29 00:00',))
_HwLswProxyArpObject_ObjectIdentity=ObjectIdentity
hwLswProxyArpObject=_HwLswProxyArpObject_ObjectIdentity((1,3,6,1,4,1,2011,2,23,1,4,1))
if mibBuilder.loadTexts:hwLswProxyArpObject.setStatus(_A)
_HwLswProxyArpEnableTable_Object=MibTable
hwLswProxyArpEnableTable=_HwLswProxyArpEnableTable_Object((1,3,6,1,4,1,2011,2,23,1,4,1,1))
if mibBuilder.loadTexts:hwLswProxyArpEnableTable.setStatus(_A)
_HwLswProxyArpEnableEntry_Object=MibTableRow
hwLswProxyArpEnableEntry=_HwLswProxyArpEnableEntry_Object((1,3,6,1,4,1,2011,2,23,1,4,1,1,1))
hwLswProxyArpEnableEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hwLswProxyArpEnableEntry.setStatus(_A)
_HwLswIfIndex_Type=Integer32
_HwLswIfIndex_Object=MibTableColumn
hwLswIfIndex=_HwLswIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,4,1,1,1,1),_HwLswIfIndex_Type())
hwLswIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:hwLswIfIndex.setStatus(_A)
class _HwLswProxyArpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_HwLswProxyArpStatus_Type.__name__=_B
_HwLswProxyArpStatus_Object=MibTableColumn
hwLswProxyArpStatus=_HwLswProxyArpStatus_Object((1,3,6,1,4,1,2011,2,23,1,4,1,1,1,2),_HwLswProxyArpStatus_Type())
hwLswProxyArpStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:hwLswProxyArpStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hwLswArpMib':hwLswArpMib,'hwLswProxyArpObject':hwLswProxyArpObject,'hwLswProxyArpEnableTable':hwLswProxyArpEnableTable,'hwLswProxyArpEnableEntry':hwLswProxyArpEnableEntry,_D:hwLswIfIndex,'hwLswProxyArpStatus':hwLswProxyArpStatus})