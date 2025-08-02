_P='detailedMessage'
_O='catalogKey'
_N='serialNumber'
_M='messageCode'
_L='timeOccurred'
_K='severity'
_J='nodeID'
_I='details'
_H='component'
_G='ThreeparLongDisplayString'
_F='DisplayString'
_E='Unsigned32'
_D='Integer32'
_C='read-only'
_B='ThreeParMIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AgentCapabilities,ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','AgentCapabilities','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
threepar=ModuleIdentity((1,3,6,1,4,1,12925))
if mibBuilder.loadTexts:threepar.setRevisions(('2014-09-18 10:00','2013-03-12 11:22','2012-08-02 15:22','2010-10-04 14:45','2007-10-05 15:00','2004-12-13 17:00','2004-12-13 16:40','2004-06-14 15:45','2002-04-16 13:27'))
class ThreeparLongDisplayString(TextualConvention,OctetString):status=_A
_Inserv_ObjectIdentity=ObjectIdentity
inserv=_Inserv_ObjectIdentity((1,3,6,1,4,1,12925,1))
if mibBuilder.loadTexts:inserv.setStatus(_A)
_InservAgentCaps_ObjectIdentity=ObjectIdentity
inservAgentCaps=_InservAgentCaps_ObjectIdentity((1,3,6,1,4,1,12925,1,4))
if mibBuilder.loadTexts:inservAgentCaps.setStatus(_A)
_AlertTable_Object=MibTable
alertTable=_AlertTable_Object((1,3,6,1,4,1,12925,1,7))
if mibBuilder.loadTexts:alertTable.setStatus(_A)
_AlertEntry_Object=MibTableRow
alertEntry=_AlertEntry_Object((1,3,6,1,4,1,12925,1,7,1))
alertEntry.setIndexNames((0,_B,'index'))
if mibBuilder.loadTexts:alertEntry.setStatus(_A)
class _Index_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_Index_Type.__name__=_D
_Index_Object=MibTableColumn
index=_Index_Object((1,3,6,1,4,1,12925,1,7,1,1),_Index_Type())
index.setMaxAccess(_C)
if mibBuilder.loadTexts:index.setStatus(_A)
class _Severity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('fatal',0),('critical',1),('major',2),('minor',3),('degraded',4),('info',5),('debug',6)))
_Severity_Type.__name__=_D
_Severity_Object=MibTableColumn
severity=_Severity_Object((1,3,6,1,4,1,12925,1,7,1,2),_Severity_Type())
severity.setMaxAccess(_C)
if mibBuilder.loadTexts:severity.setStatus(_A)
_TimeOccurred_Type=DisplayString
_TimeOccurred_Object=MibTableColumn
timeOccurred=_TimeOccurred_Object((1,3,6,1,4,1,12925,1,7,1,3),_TimeOccurred_Type())
timeOccurred.setMaxAccess(_C)
if mibBuilder.loadTexts:timeOccurred.setStatus(_A)
class _NodeID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_NodeID_Type.__name__=_E
_NodeID_Object=MibTableColumn
nodeID=_NodeID_Object((1,3,6,1,4,1,12925,1,7,1,4),_NodeID_Type())
nodeID.setMaxAccess(_C)
if mibBuilder.loadTexts:nodeID.setStatus(_A)
class _Component_Type(DisplayString):defaultValue=OctetString('1')
_Component_Type.__name__=_F
_Component_Object=MibTableColumn
component=_Component_Object((1,3,6,1,4,1,12925,1,7,1,5),_Component_Type())
component.setMaxAccess(_C)
if mibBuilder.loadTexts:component.setStatus(_A)
class _Details_Type(ThreeparLongDisplayString):subtypeSpec=ThreeparLongDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,511))
_Details_Type.__name__=_G
_Details_Object=MibTableColumn
details=_Details_Object((1,3,6,1,4,1,12925,1,7,1,6),_Details_Type())
details.setMaxAccess(_C)
if mibBuilder.loadTexts:details.setStatus(_A)
class _Id_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_Id_Type.__name__=_E
_Id_Object=MibTableColumn
id=_Id_Object((1,3,6,1,4,1,12925,1,7,1,7),_Id_Type())
id.setMaxAccess(_C)
if mibBuilder.loadTexts:id.setStatus(_A)
class _MessageCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(65537,4294967295))
_MessageCode_Type.__name__=_E
_MessageCode_Object=MibTableColumn
messageCode=_MessageCode_Object((1,3,6,1,4,1,12925,1,7,1,8),_MessageCode_Type())
messageCode.setMaxAccess(_C)
if mibBuilder.loadTexts:messageCode.setStatus(_A)
class _State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('undefined',0),('new',1),('acknowledged',2),('fixed',3),('removed',4),('autofixed',5)))
_State_Type.__name__=_D
_State_Object=MibTableColumn
state=_State_Object((1,3,6,1,4,1,12925,1,7,1,9),_State_Type())
state.setMaxAccess(_C)
if mibBuilder.loadTexts:state.setStatus(_A)
_SerialNumber_Type=DisplayString
_SerialNumber_Object=MibTableColumn
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,12925,1,7,1,10),_SerialNumber_Type())
serialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_CatalogKey_Type=DisplayString
_CatalogKey_Object=MibTableColumn
catalogKey=_CatalogKey_Object((1,3,6,1,4,1,12925,1,7,1,11),_CatalogKey_Type())
catalogKey.setMaxAccess(_C)
if mibBuilder.loadTexts:catalogKey.setStatus(_A)
_DetailedMessage_Type=DisplayString
_DetailedMessage_Object=MibTableColumn
detailedMessage=_DetailedMessage_Object((1,3,6,1,4,1,12925,1,7,1,12),_DetailedMessage_Type())
detailedMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:detailedMessage.setStatus(_A)
alertNotify=NotificationType((1,3,6,1,4,1,12925,1,8))
alertNotify.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,'id'),(_B,_M),(_B,'state'),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:alertNotify.setStatus(_A)
inservAgentCapability=AgentCapabilities((1,3,6,1,4,1,12925,1,4,1))
if mibBuilder.loadTexts:inservAgentCapability.setProductRelease('InServ Release 2.2')
if mibBuilder.loadTexts:inservAgentCapability.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_G:ThreeparLongDisplayString,'threepar':threepar,'inserv':inserv,'inservAgentCaps':inservAgentCaps,'inservAgentCapability':inservAgentCapability,'alertTable':alertTable,'alertEntry':alertEntry,'index':index,_K:severity,_L:timeOccurred,_J:nodeID,_H:component,_I:details,'id':id,_M:messageCode,'state':state,_N:serialNumber,_O:catalogKey,_P:detailedMessage,'alertNotify':alertNotify})