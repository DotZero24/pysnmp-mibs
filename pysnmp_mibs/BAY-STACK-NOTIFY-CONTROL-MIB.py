_E='bsncNotifyControlType'
_D='BAY-STACK-NOTIFY-CONTROL-MIB'
_C='TruthValue'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_C)
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackNotifyControlMib=ModuleIdentity((1,3,6,1,4,1,45,5,31))
if mibBuilder.loadTexts:bayStackNotifyControlMib.setRevisions(('2010-09-08 00:00','2008-10-17 00:00'))
_BsncObjects_ObjectIdentity=ObjectIdentity
bsncObjects=_BsncObjects_ObjectIdentity((1,3,6,1,4,1,45,5,31,1))
_BsncNotifyControlTable_Object=MibTable
bsncNotifyControlTable=_BsncNotifyControlTable_Object((1,3,6,1,4,1,45,5,31,1,1))
if mibBuilder.loadTexts:bsncNotifyControlTable.setStatus(_A)
_BsncNotifyControlEntry_Object=MibTableRow
bsncNotifyControlEntry=_BsncNotifyControlEntry_Object((1,3,6,1,4,1,45,5,31,1,1,1))
bsncNotifyControlEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:bsncNotifyControlEntry.setStatus(_A)
_BsncNotifyControlType_Type=ObjectIdentifier
_BsncNotifyControlType_Object=MibTableColumn
bsncNotifyControlType=_BsncNotifyControlType_Object((1,3,6,1,4,1,45,5,31,1,1,1,1),_BsncNotifyControlType_Type())
bsncNotifyControlType.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bsncNotifyControlType.setStatus(_A)
class _BsncNotifyControlEnabled_Type(TruthValue):defaultValue=1
_BsncNotifyControlEnabled_Type.__name__=_C
_BsncNotifyControlEnabled_Object=MibTableColumn
bsncNotifyControlEnabled=_BsncNotifyControlEnabled_Object((1,3,6,1,4,1,45,5,31,1,1,1,2),_BsncNotifyControlEnabled_Type())
bsncNotifyControlEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bsncNotifyControlEnabled.setStatus(_A)
_BsncNotifyControlRowStatus_Type=RowStatus
_BsncNotifyControlRowStatus_Object=MibTableColumn
bsncNotifyControlRowStatus=_BsncNotifyControlRowStatus_Object((1,3,6,1,4,1,45,5,31,1,1,1,3),_BsncNotifyControlRowStatus_Type())
bsncNotifyControlRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bsncNotifyControlRowStatus.setStatus(_A)
_BsncNotifyControlPortListEnabled_Type=PortList
_BsncNotifyControlPortListEnabled_Object=MibTableColumn
bsncNotifyControlPortListEnabled=_BsncNotifyControlPortListEnabled_Object((1,3,6,1,4,1,45,5,31,1,1,1,4),_BsncNotifyControlPortListEnabled_Type())
bsncNotifyControlPortListEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bsncNotifyControlPortListEnabled.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bayStackNotifyControlMib':bayStackNotifyControlMib,'bsncObjects':bsncObjects,'bsncNotifyControlTable':bsncNotifyControlTable,'bsncNotifyControlEntry':bsncNotifyControlEntry,_E:bsncNotifyControlType,'bsncNotifyControlEnabled':bsncNotifyControlEnabled,'bsncNotifyControlRowStatus':bsncNotifyControlRowStatus,'bsncNotifyControlPortListEnabled':bsncNotifyControlPortListEnabled})