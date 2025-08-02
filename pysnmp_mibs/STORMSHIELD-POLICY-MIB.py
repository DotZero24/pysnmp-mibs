_E='snsPolicyIndex'
_D='STORMSHIELD-POLICY-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
stormshieldMIB,=mibBuilder.importSymbols('STORMSHIELD-SMI-MIB','stormshieldMIB')
snsPolicy=ModuleIdentity((1,3,6,1,4,1,11256,1,8))
if mibBuilder.loadTexts:snsPolicy.setRevisions(('2017-02-20 00:00',))
_SnsPolicyTable_Object=MibTable
snsPolicyTable=_SnsPolicyTable_Object((1,3,6,1,4,1,11256,1,8,1))
if mibBuilder.loadTexts:snsPolicyTable.setStatus(_A)
_SnsPolicyEntry_Object=MibTableRow
snsPolicyEntry=_SnsPolicyEntry_Object((1,3,6,1,4,1,11256,1,8,1,1))
snsPolicyEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:snsPolicyEntry.setStatus(_A)
class _SnsPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnsPolicyIndex_Type.__name__=_C
_SnsPolicyIndex_Object=MibTableColumn
snsPolicyIndex=_SnsPolicyIndex_Object((1,3,6,1,4,1,11256,1,8,1,1,1),_SnsPolicyIndex_Type())
snsPolicyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snsPolicyIndex.setStatus(_A)
_SnsPolicyName_Type=SnmpAdminString
_SnsPolicyName_Object=MibTableColumn
snsPolicyName=_SnsPolicyName_Object((1,3,6,1,4,1,11256,1,8,1,1,2),_SnsPolicyName_Type())
snsPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsPolicyName.setStatus(_A)
_SnsPolicySlotName_Type=SnmpAdminString
_SnsPolicySlotName_Object=MibTableColumn
snsPolicySlotName=_SnsPolicySlotName_Object((1,3,6,1,4,1,11256,1,8,1,1,3),_SnsPolicySlotName_Type())
snsPolicySlotName.setMaxAccess(_B)
if mibBuilder.loadTexts:snsPolicySlotName.setStatus(_A)
_SnsPolicyActive_Type=DisplayString
_SnsPolicyActive_Object=MibTableColumn
snsPolicyActive=_SnsPolicyActive_Object((1,3,6,1,4,1,11256,1,8,1,1,4),_SnsPolicyActive_Type())
snsPolicyActive.setMaxAccess(_B)
if mibBuilder.loadTexts:snsPolicyActive.setStatus(_A)
_SnsPolicySync_Type=Integer32
_SnsPolicySync_Object=MibTableColumn
snsPolicySync=_SnsPolicySync_Object((1,3,6,1,4,1,11256,1,8,1,1,5),_SnsPolicySync_Type())
snsPolicySync.setMaxAccess(_B)
if mibBuilder.loadTexts:snsPolicySync.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'snsPolicy':snsPolicy,'snsPolicyTable':snsPolicyTable,'snsPolicyEntry':snsPolicyEntry,_E:snsPolicyIndex,'snsPolicyName':snsPolicyName,'snsPolicySlotName':snsPolicySlotName,'snsPolicyActive':snsPolicyActive,'snsPolicySync':snsPolicySync})