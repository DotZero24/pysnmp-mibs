_E='dot1xPortEntry'
_D='RAISECOM-DOT1X-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1xPaePortEntry,=mibBuilder.importSymbols('IEEE8021-PAE-MIB','dot1xPaePortEntry')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rcDot1x=ModuleIdentity((1,3,6,1,4,1,8886,6,1,27))
_RcDot1xObjects_ObjectIdentity=ObjectIdentity
rcDot1xObjects=_RcDot1xObjects_ObjectIdentity((1,3,6,1,4,1,8886,6,1,27,1))
_RcDot1xConfig_ObjectIdentity=ObjectIdentity
rcDot1xConfig=_RcDot1xConfig_ObjectIdentity((1,3,6,1,4,1,8886,6,1,27,1,1))
_Dot1xPortTable_Object=MibTable
dot1xPortTable=_Dot1xPortTable_Object((1,3,6,1,4,1,8886,6,1,27,1,1,1))
if mibBuilder.loadTexts:dot1xPortTable.setStatus(_A)
_Dot1xPortEntry_Object=MibTableRow
dot1xPortEntry=_Dot1xPortEntry_Object((1,3,6,1,4,1,8886,6,1,27,1,1,1,1))
if mibBuilder.loadTexts:dot1xPortEntry.setStatus(_A)
class _Rcdot1xPortAuthControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_Rcdot1xPortAuthControl_Type.__name__=_B
_Rcdot1xPortAuthControl_Object=MibTableColumn
rcdot1xPortAuthControl=_Rcdot1xPortAuthControl_Object((1,3,6,1,4,1,8886,6,1,27,1,1,1,1,1),_Rcdot1xPortAuthControl_Type())
rcdot1xPortAuthControl.setMaxAccess(_C)
if mibBuilder.loadTexts:rcdot1xPortAuthControl.setStatus(_A)
_Rcdot1xPortStatisticClear_Type=TruthValue
_Rcdot1xPortStatisticClear_Object=MibTableColumn
rcdot1xPortStatisticClear=_Rcdot1xPortStatisticClear_Object((1,3,6,1,4,1,8886,6,1,27,1,1,1,1,2),_Rcdot1xPortStatisticClear_Type())
rcdot1xPortStatisticClear.setMaxAccess(_C)
if mibBuilder.loadTexts:rcdot1xPortStatisticClear.setStatus(_A)
class _Rcdot1xPortAuthMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portbased',1),('macbased',2)))
_Rcdot1xPortAuthMethod_Type.__name__=_B
_Rcdot1xPortAuthMethod_Object=MibTableColumn
rcdot1xPortAuthMethod=_Rcdot1xPortAuthMethod_Object((1,3,6,1,4,1,8886,6,1,27,1,1,1,1,3),_Rcdot1xPortAuthMethod_Type())
rcdot1xPortAuthMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:rcdot1xPortAuthMethod.setStatus(_A)
dot1xPaePortEntry.registerAugmentions((_D,_E))
dot1xPortEntry.setIndexNames(*dot1xPaePortEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'rcDot1x':rcDot1x,'rcDot1xObjects':rcDot1xObjects,'rcDot1xConfig':rcDot1xConfig,'dot1xPortTable':dot1xPortTable,_E:dot1xPortEntry,'rcdot1xPortAuthControl':rcdot1xPortAuthControl,'rcdot1xPortStatisticClear':rcdot1xPortStatisticClear,'rcdot1xPortAuthMethod':rcdot1xPortAuthMethod})