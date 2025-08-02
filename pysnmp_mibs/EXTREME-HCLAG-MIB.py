_E='extremeHclagMemberPort'
_D='extremeHclagGroup'
_C='EXTREME-HCLAG-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
extremeHclag=ModuleIdentity((1,3,6,1,4,1,1916,1,38))
class HclagGroupId(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class HclagMemberPort(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_ExtremeHclagTable_Object=MibTable
extremeHclagTable=_ExtremeHclagTable_Object((1,3,6,1,4,1,1916,1,38,1))
if mibBuilder.loadTexts:extremeHclagTable.setStatus(_A)
_ExtremeHclagEntry_Object=MibTableRow
extremeHclagEntry=_ExtremeHclagEntry_Object((1,3,6,1,4,1,1916,1,38,1,1))
extremeHclagEntry.setIndexNames((0,_C,_D),(0,_C,_E))
if mibBuilder.loadTexts:extremeHclagEntry.setStatus(_A)
_ExtremeHclagGroup_Type=HclagGroupId
_ExtremeHclagGroup_Object=MibTableColumn
extremeHclagGroup=_ExtremeHclagGroup_Object((1,3,6,1,4,1,1916,1,38,1,1,1),_ExtremeHclagGroup_Type())
extremeHclagGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeHclagGroup.setStatus(_A)
_ExtremeHclagMemberPort_Type=HclagMemberPort
_ExtremeHclagMemberPort_Object=MibTableColumn
extremeHclagMemberPort=_ExtremeHclagMemberPort_Object((1,3,6,1,4,1,1916,1,38,1,1,2),_ExtremeHclagMemberPort_Type())
extremeHclagMemberPort.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeHclagMemberPort.setStatus(_A)
_ExtremeHclagAdminState_Type=TruthValue
_ExtremeHclagAdminState_Object=MibTableColumn
extremeHclagAdminState=_ExtremeHclagAdminState_Object((1,3,6,1,4,1,1916,1,38,1,1,3),_ExtremeHclagAdminState_Type())
extremeHclagAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeHclagAdminState.setStatus(_A)
_ExtremeHclagLinkState_Type=TruthValue
_ExtremeHclagLinkState_Object=MibTableColumn
extremeHclagLinkState=_ExtremeHclagLinkState_Object((1,3,6,1,4,1,1916,1,38,1,1,4),_ExtremeHclagLinkState_Type())
extremeHclagLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeHclagLinkState.setStatus(_A)
_ExtremeHclagStatus_Type=TruthValue
_ExtremeHclagStatus_Object=MibTableColumn
extremeHclagStatus=_ExtremeHclagStatus_Object((1,3,6,1,4,1,1916,1,38,1,1,5),_ExtremeHclagStatus_Type())
extremeHclagStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeHclagStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'HclagGroupId':HclagGroupId,'HclagMemberPort':HclagMemberPort,'extremeHclag':extremeHclag,'extremeHclagTable':extremeHclagTable,'extremeHclagEntry':extremeHclagEntry,_D:extremeHclagGroup,_E:extremeHclagMemberPort,'extremeHclagAdminState':extremeHclagAdminState,'extremeHclagLinkState':extremeHclagLinkState,'extremeHclagStatus':extremeHclagStatus})