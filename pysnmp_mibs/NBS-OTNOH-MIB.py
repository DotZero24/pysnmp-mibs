_H='not-accessible'
_G='nbsOtnohTtiScope'
_F='nbsOtnohTtiIfIndex'
_E='Integer32'
_D='NBS-OTNOH-MIB'
_C='read-create'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
nbs,=mibBuilder.importSymbols('NBS-MIB','nbs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
nbsOtnohMib=ModuleIdentity((1,3,6,1,4,1,629,224))
_NbsOtnohTtiGrp_ObjectIdentity=ObjectIdentity
nbsOtnohTtiGrp=_NbsOtnohTtiGrp_ObjectIdentity((1,3,6,1,4,1,629,224,1))
if mibBuilder.loadTexts:nbsOtnohTtiGrp.setStatus(_A)
_NbsOtnohTtiTable_Object=MibTable
nbsOtnohTtiTable=_NbsOtnohTtiTable_Object((1,3,6,1,4,1,629,224,1,1))
if mibBuilder.loadTexts:nbsOtnohTtiTable.setStatus(_A)
_NbsOtnohTtiEntry_Object=MibTableRow
nbsOtnohTtiEntry=_NbsOtnohTtiEntry_Object((1,3,6,1,4,1,629,224,1,1,1))
nbsOtnohTtiEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:nbsOtnohTtiEntry.setStatus(_A)
_NbsOtnohTtiIfIndex_Type=InterfaceIndex
_NbsOtnohTtiIfIndex_Object=MibTableColumn
nbsOtnohTtiIfIndex=_NbsOtnohTtiIfIndex_Object((1,3,6,1,4,1,629,224,1,1,1,1),_NbsOtnohTtiIfIndex_Type())
nbsOtnohTtiIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsOtnohTtiIfIndex.setStatus(_A)
class _NbsOtnohTtiScope_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('tcm1',1),('tcm2',2),('tcm3',3),('tcm4',4),('tcm5',5),('tcm6',6),('section',7),('path',8)))
_NbsOtnohTtiScope_Type.__name__=_E
_NbsOtnohTtiScope_Object=MibTableColumn
nbsOtnohTtiScope=_NbsOtnohTtiScope_Object((1,3,6,1,4,1,629,224,1,1,1,2),_NbsOtnohTtiScope_Type())
nbsOtnohTtiScope.setMaxAccess(_H)
if mibBuilder.loadTexts:nbsOtnohTtiScope.setStatus(_A)
class _NbsOtnohTtiSendSapi_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsOtnohTtiSendSapi_Type.__name__=_B
_NbsOtnohTtiSendSapi_Object=MibTableColumn
nbsOtnohTtiSendSapi=_NbsOtnohTtiSendSapi_Object((1,3,6,1,4,1,629,224,1,1,1,3),_NbsOtnohTtiSendSapi_Type())
nbsOtnohTtiSendSapi.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOtnohTtiSendSapi.setStatus(_A)
class _NbsOtnohTtiSendDapi_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsOtnohTtiSendDapi_Type.__name__=_B
_NbsOtnohTtiSendDapi_Object=MibTableColumn
nbsOtnohTtiSendDapi=_NbsOtnohTtiSendDapi_Object((1,3,6,1,4,1,629,224,1,1,1,4),_NbsOtnohTtiSendDapi_Type())
nbsOtnohTtiSendDapi.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOtnohTtiSendDapi.setStatus(_A)
class _NbsOtnohTtiSendOpSpec_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NbsOtnohTtiSendOpSpec_Type.__name__=_B
_NbsOtnohTtiSendOpSpec_Object=MibTableColumn
nbsOtnohTtiSendOpSpec=_NbsOtnohTtiSendOpSpec_Object((1,3,6,1,4,1,629,224,1,1,1,5),_NbsOtnohTtiSendOpSpec_Type())
nbsOtnohTtiSendOpSpec.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOtnohTtiSendOpSpec.setStatus(_A)
class _NbsOtnohTtiExpectSapi_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsOtnohTtiExpectSapi_Type.__name__=_B
_NbsOtnohTtiExpectSapi_Object=MibTableColumn
nbsOtnohTtiExpectSapi=_NbsOtnohTtiExpectSapi_Object((1,3,6,1,4,1,629,224,1,1,1,6),_NbsOtnohTtiExpectSapi_Type())
nbsOtnohTtiExpectSapi.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOtnohTtiExpectSapi.setStatus(_A)
class _NbsOtnohTtiExpectDapi_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_NbsOtnohTtiExpectDapi_Type.__name__=_B
_NbsOtnohTtiExpectDapi_Object=MibTableColumn
nbsOtnohTtiExpectDapi=_NbsOtnohTtiExpectDapi_Object((1,3,6,1,4,1,629,224,1,1,1,7),_NbsOtnohTtiExpectDapi_Type())
nbsOtnohTtiExpectDapi.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOtnohTtiExpectDapi.setStatus(_A)
class _NbsOtnohTtiExpectOpSpec_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NbsOtnohTtiExpectOpSpec_Type.__name__=_B
_NbsOtnohTtiExpectOpSpec_Object=MibTableColumn
nbsOtnohTtiExpectOpSpec=_NbsOtnohTtiExpectOpSpec_Object((1,3,6,1,4,1,629,224,1,1,1,8),_NbsOtnohTtiExpectOpSpec_Type())
nbsOtnohTtiExpectOpSpec.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOtnohTtiExpectOpSpec.setStatus(_A)
_NbsOtnohTtiRowStatus_Type=RowStatus
_NbsOtnohTtiRowStatus_Object=MibTableColumn
nbsOtnohTtiRowStatus=_NbsOtnohTtiRowStatus_Object((1,3,6,1,4,1,629,224,1,1,1,10),_NbsOtnohTtiRowStatus_Type())
nbsOtnohTtiRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbsOtnohTtiRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nbsOtnohMib':nbsOtnohMib,'nbsOtnohTtiGrp':nbsOtnohTtiGrp,'nbsOtnohTtiTable':nbsOtnohTtiTable,'nbsOtnohTtiEntry':nbsOtnohTtiEntry,_F:nbsOtnohTtiIfIndex,_G:nbsOtnohTtiScope,'nbsOtnohTtiSendSapi':nbsOtnohTtiSendSapi,'nbsOtnohTtiSendDapi':nbsOtnohTtiSendDapi,'nbsOtnohTtiSendOpSpec':nbsOtnohTtiSendOpSpec,'nbsOtnohTtiExpectSapi':nbsOtnohTtiExpectSapi,'nbsOtnohTtiExpectDapi':nbsOtnohTtiExpectDapi,'nbsOtnohTtiExpectOpSpec':nbsOtnohTtiExpectOpSpec,'nbsOtnohTtiRowStatus':nbsOtnohTtiRowStatus})