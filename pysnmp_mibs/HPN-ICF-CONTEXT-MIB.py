_F='DisplayString'
_E='Integer32'
_D='hpnicfContextName'
_C='hpnicfContextIndex'
_B='HPN-ICF-CONTEXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
hpnicfContext=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,154))
if mibBuilder.loadTexts:hpnicfContext.setRevisions(('2014-03-18 00:00',))
_HpnicfContextTables_ObjectIdentity=ObjectIdentity
hpnicfContextTables=_HpnicfContextTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,154,1))
_HpnicfContextControl_ObjectIdentity=ObjectIdentity
hpnicfContextControl=_HpnicfContextControl_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,154,1,1))
_HpnicfContextControlTable_Object=MibTable
hpnicfContextControlTable=_HpnicfContextControlTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,154,1,1,1))
if mibBuilder.loadTexts:hpnicfContextControlTable.setStatus(_A)
_HpnicfContextControlEntry_Object=MibTableRow
hpnicfContextControlEntry=_HpnicfContextControlEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,154,1,1,1,1))
hpnicfContextControlEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:hpnicfContextControlEntry.setStatus(_A)
class _HpnicfContextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfContextIndex_Type.__name__=_E
_HpnicfContextIndex_Object=MibTableColumn
hpnicfContextIndex=_HpnicfContextIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,154,1,1,1,1,1),_HpnicfContextIndex_Type())
hpnicfContextIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:hpnicfContextIndex.setStatus(_A)
class _HpnicfContextName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_HpnicfContextName_Type.__name__=_F
_HpnicfContextName_Object=MibTableColumn
hpnicfContextName=_HpnicfContextName_Object((1,3,6,1,4,1,11,2,14,11,15,2,154,1,1,1,1,2),_HpnicfContextName_Type())
hpnicfContextName.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfContextName.setStatus(_A)
_HpnicfContextNotification_ObjectIdentity=ObjectIdentity
hpnicfContextNotification=_HpnicfContextNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,154,8))
_HpnicfContextNotificationObjects_ObjectIdentity=ObjectIdentity
hpnicfContextNotificationObjects=_HpnicfContextNotificationObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,154,8,0))
hpnicfContextStateChangeToActive=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,154,8,0,1))
hpnicfContextStateChangeToActive.setObjects(*((_B,_C),(_B,_D)))
if mibBuilder.loadTexts:hpnicfContextStateChangeToActive.setStatus(_A)
hpnicfContextStateChangeToInactive=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,154,8,0,2))
hpnicfContextStateChangeToInactive.setObjects(*((_B,_C),(_B,_D)))
if mibBuilder.loadTexts:hpnicfContextStateChangeToInactive.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfContext':hpnicfContext,'hpnicfContextTables':hpnicfContextTables,'hpnicfContextControl':hpnicfContextControl,'hpnicfContextControlTable':hpnicfContextControlTable,'hpnicfContextControlEntry':hpnicfContextControlEntry,_C:hpnicfContextIndex,_D:hpnicfContextName,'hpnicfContextNotification':hpnicfContextNotification,'hpnicfContextNotificationObjects':hpnicfContextNotificationObjects,'hpnicfContextStateChangeToActive':hpnicfContextStateChangeToActive,'hpnicfContextStateChangeToInactive':hpnicfContextStateChangeToInactive})