_F='DisplayString'
_E='Integer32'
_D='h3cContextName'
_C='h3cContextIndex'
_B='H3C-CONTEXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
h3cContext=ModuleIdentity((1,3,6,1,4,1,2011,10,2,154))
if mibBuilder.loadTexts:h3cContext.setRevisions(('2014-03-18 00:00',))
_H3cContextTables_ObjectIdentity=ObjectIdentity
h3cContextTables=_H3cContextTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,154,1))
_H3cContextControl_ObjectIdentity=ObjectIdentity
h3cContextControl=_H3cContextControl_ObjectIdentity((1,3,6,1,4,1,2011,10,2,154,1,1))
_H3cContextControlTable_Object=MibTable
h3cContextControlTable=_H3cContextControlTable_Object((1,3,6,1,4,1,2011,10,2,154,1,1,1))
if mibBuilder.loadTexts:h3cContextControlTable.setStatus(_A)
_H3cContextControlEntry_Object=MibTableRow
h3cContextControlEntry=_H3cContextControlEntry_Object((1,3,6,1,4,1,2011,10,2,154,1,1,1,1))
h3cContextControlEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:h3cContextControlEntry.setStatus(_A)
class _H3cContextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cContextIndex_Type.__name__=_E
_H3cContextIndex_Object=MibTableColumn
h3cContextIndex=_H3cContextIndex_Object((1,3,6,1,4,1,2011,10,2,154,1,1,1,1,1),_H3cContextIndex_Type())
h3cContextIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cContextIndex.setStatus(_A)
class _H3cContextName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_H3cContextName_Type.__name__=_F
_H3cContextName_Object=MibTableColumn
h3cContextName=_H3cContextName_Object((1,3,6,1,4,1,2011,10,2,154,1,1,1,1,2),_H3cContextName_Type())
h3cContextName.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cContextName.setStatus(_A)
_H3cContextNotification_ObjectIdentity=ObjectIdentity
h3cContextNotification=_H3cContextNotification_ObjectIdentity((1,3,6,1,4,1,2011,10,2,154,8))
_H3cContextNotificationObjects_ObjectIdentity=ObjectIdentity
h3cContextNotificationObjects=_H3cContextNotificationObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,154,8,0))
h3cContextStateChangeToActive=NotificationType((1,3,6,1,4,1,2011,10,2,154,8,0,1))
h3cContextStateChangeToActive.setObjects(*((_B,_C),(_B,_D)))
if mibBuilder.loadTexts:h3cContextStateChangeToActive.setStatus(_A)
h3cContextStateChangeToInactive=NotificationType((1,3,6,1,4,1,2011,10,2,154,8,0,2))
h3cContextStateChangeToInactive.setObjects(*((_B,_C),(_B,_D)))
if mibBuilder.loadTexts:h3cContextStateChangeToInactive.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cContext':h3cContext,'h3cContextTables':h3cContextTables,'h3cContextControl':h3cContextControl,'h3cContextControlTable':h3cContextControlTable,'h3cContextControlEntry':h3cContextControlEntry,_C:h3cContextIndex,_D:h3cContextName,'h3cContextNotification':h3cContextNotification,'h3cContextNotificationObjects':h3cContextNotificationObjects,'h3cContextStateChangeToActive':h3cContextStateChangeToActive,'h3cContextStateChangeToInactive':h3cContextStateChangeToInactive})