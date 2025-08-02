_E='snsAutoupdateIndex'
_D='STORMSHIELD-AUTOUPDATE-MIB'
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
snsAutoupdate=ModuleIdentity((1,3,6,1,4,1,11256,1,9))
if mibBuilder.loadTexts:snsAutoupdate.setRevisions(('2017-02-20 00:00',))
_SnsAutoupdateTable_Object=MibTable
snsAutoupdateTable=_SnsAutoupdateTable_Object((1,3,6,1,4,1,11256,1,9,1))
if mibBuilder.loadTexts:snsAutoupdateTable.setStatus(_A)
_SnsAutoupdateEntry_Object=MibTableRow
snsAutoupdateEntry=_SnsAutoupdateEntry_Object((1,3,6,1,4,1,11256,1,9,1,1))
snsAutoupdateEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:snsAutoupdateEntry.setStatus(_A)
class _SnsAutoupdateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnsAutoupdateIndex_Type.__name__=_C
_SnsAutoupdateIndex_Object=MibTableColumn
snsAutoupdateIndex=_SnsAutoupdateIndex_Object((1,3,6,1,4,1,11256,1,9,1,1,1),_SnsAutoupdateIndex_Type())
snsAutoupdateIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAutoupdateIndex.setStatus(_A)
_SnsAutoupdateSubsys_Type=SnmpAdminString
_SnsAutoupdateSubsys_Object=MibTableColumn
snsAutoupdateSubsys=_SnsAutoupdateSubsys_Object((1,3,6,1,4,1,11256,1,9,1,1,2),_SnsAutoupdateSubsys_Type())
snsAutoupdateSubsys.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAutoupdateSubsys.setStatus(_A)
_SnsAutoupdateState_Type=DisplayString
_SnsAutoupdateState_Object=MibTableColumn
snsAutoupdateState=_SnsAutoupdateState_Object((1,3,6,1,4,1,11256,1,9,1,1,3),_SnsAutoupdateState_Type())
snsAutoupdateState.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAutoupdateState.setStatus(_A)
_SnsAutoupdateLast_Type=DisplayString
_SnsAutoupdateLast_Object=MibTableColumn
snsAutoupdateLast=_SnsAutoupdateLast_Object((1,3,6,1,4,1,11256,1,9,1,1,4),_SnsAutoupdateLast_Type())
snsAutoupdateLast.setMaxAccess(_B)
if mibBuilder.loadTexts:snsAutoupdateLast.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'snsAutoupdate':snsAutoupdate,'snsAutoupdateTable':snsAutoupdateTable,'snsAutoupdateEntry':snsAutoupdateEntry,_E:snsAutoupdateIndex,'snsAutoupdateSubsys':snsAutoupdateSubsys,'snsAutoupdateState':snsAutoupdateState,'snsAutoupdateLast':snsAutoupdateLast})