_D='hpnicfLswIfIndex'
_C='HPN-ICF-LswARP-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicflswCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicflswCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfLswArpMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,4))
if mibBuilder.loadTexts:hpnicfLswArpMib.setRevisions(('2001-06-29 00:00',))
_HpnicfLswProxyArpObject_ObjectIdentity=ObjectIdentity
hpnicfLswProxyArpObject=_HpnicfLswProxyArpObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,4,1))
if mibBuilder.loadTexts:hpnicfLswProxyArpObject.setStatus(_A)
_HpnicfLswProxyArpEnableTable_Object=MibTable
hpnicfLswProxyArpEnableTable=_HpnicfLswProxyArpEnableTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,4,1,1))
if mibBuilder.loadTexts:hpnicfLswProxyArpEnableTable.setStatus(_A)
_HpnicfLswProxyArpEnableEntry_Object=MibTableRow
hpnicfLswProxyArpEnableEntry=_HpnicfLswProxyArpEnableEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,4,1,1,1))
hpnicfLswProxyArpEnableEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:hpnicfLswProxyArpEnableEntry.setStatus(_A)
_HpnicfLswIfIndex_Type=Integer32
_HpnicfLswIfIndex_Object=MibTableColumn
hpnicfLswIfIndex=_HpnicfLswIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,4,1,1,1,1),_HpnicfLswIfIndex_Type())
hpnicfLswIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfLswIfIndex.setStatus(_A)
class _HpnicfLswProxyArpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disabled',0),('enabled',1)))
_HpnicfLswProxyArpStatus_Type.__name__=_B
_HpnicfLswProxyArpStatus_Object=MibTableColumn
hpnicfLswProxyArpStatus=_HpnicfLswProxyArpStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,4,1,1,1,2),_HpnicfLswProxyArpStatus_Type())
hpnicfLswProxyArpStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfLswProxyArpStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfLswArpMib':hpnicfLswArpMib,'hpnicfLswProxyArpObject':hpnicfLswProxyArpObject,'hpnicfLswProxyArpEnableTable':hpnicfLswProxyArpEnableTable,'hpnicfLswProxyArpEnableEntry':hpnicfLswProxyArpEnableEntry,_D:hpnicfLswIfIndex,'hpnicfLswProxyArpStatus':hpnicfLswProxyArpStatus})