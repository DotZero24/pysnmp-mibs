_M='tsoutStatusID'
_L='transcoding'
_K='fullDpmControl'
_J='mapPassthrough'
_I='passThrough'
_H='noOutput'
_G='tsoutID'
_F='CISCO-DMN-DSG-TSOUT-MIB'
_E='DisplayString'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
ciscoDSGTSOUT=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,34))
if mibBuilder.loadTexts:ciscoDSGTSOUT.setRevisions(('2012-03-20 11:00','2010-08-24 07:30'))
_TsoutTable_Object=MibTable
tsoutTable=_TsoutTable_Object((1,3,6,1,4,1,1429,2,2,5,34,1))
if mibBuilder.loadTexts:tsoutTable.setStatus(_A)
_TsoutEntry_Object=MibTableRow
tsoutEntry=_TsoutEntry_Object((1,3,6,1,4,1,1429,2,2,5,34,1,1))
tsoutEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:tsoutEntry.setStatus(_A)
class _TsoutID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_TsoutID_Type.__name__=_B
_TsoutID_Object=MibTableColumn
tsoutID=_TsoutID_Object((1,3,6,1,4,1,1429,2,2,5,34,1,1,1),_TsoutID_Type())
tsoutID.setMaxAccess(_D)
if mibBuilder.loadTexts:tsoutID.setStatus(_A)
class _TsoutInstanceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TsoutInstanceName_Type.__name__=_E
_TsoutInstanceName_Object=MibTableColumn
tsoutInstanceName=_TsoutInstanceName_Object((1,3,6,1,4,1,1429,2,2,5,34,1,1,2),_TsoutInstanceName_Type())
tsoutInstanceName.setMaxAccess(_D)
if mibBuilder.loadTexts:tsoutInstanceName.setStatus(_A)
class _TsoutOutputMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_H,1),(_I,2),('serviceChannelOnly',3),(_J,4),('mapserviceChannelOnly',5),(_K,6),(_L,7)))
_TsoutOutputMode_Type.__name__=_B
_TsoutOutputMode_Object=MibTableColumn
tsoutOutputMode=_TsoutOutputMode_Object((1,3,6,1,4,1,1429,2,2,5,34,1,1,3),_TsoutOutputMode_Type())
tsoutOutputMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tsoutOutputMode.setStatus(_A)
class _TsoutDescrambleMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deScrambled',1),('scrambled',2)))
_TsoutDescrambleMode_Type.__name__=_B
_TsoutDescrambleMode_Object=MibTableColumn
tsoutDescrambleMode=_TsoutDescrambleMode_Object((1,3,6,1,4,1,1429,2,2,5,34,1,1,4),_TsoutDescrambleMode_Type())
tsoutDescrambleMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tsoutDescrambleMode.setStatus(_A)
class _TsoutRateControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('user',2)))
_TsoutRateControl_Type.__name__=_B
_TsoutRateControl_Object=MibTableColumn
tsoutRateControl=_TsoutRateControl_Object((1,3,6,1,4,1,1429,2,2,5,34,1,1,5),_TsoutRateControl_Type())
tsoutRateControl.setMaxAccess(_C)
if mibBuilder.loadTexts:tsoutRateControl.setStatus(_A)
class _TsoutOutputRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,206000000))
_TsoutOutputRate_Type.__name__=_B
_TsoutOutputRate_Object=MibTableColumn
tsoutOutputRate=_TsoutOutputRate_Object((1,3,6,1,4,1,1429,2,2,5,34,1,1,6),_TsoutOutputRate_Type())
tsoutOutputRate.setMaxAccess(_C)
if mibBuilder.loadTexts:tsoutOutputRate.setStatus(_A)
class _TsoutInsertNullPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no',1),('yes',2)))
_TsoutInsertNullPkt_Type.__name__=_B
_TsoutInsertNullPkt_Object=MibTableColumn
tsoutInsertNullPkt=_TsoutInsertNullPkt_Object((1,3,6,1,4,1,1429,2,2,5,34,1,1,7),_TsoutInsertNullPkt_Type())
tsoutInsertNullPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:tsoutInsertNullPkt.setStatus(_A)
class _TsoutMOIPOutputMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_H,1),(_I,2),('serviceChannelsOnly',3),(_J,4),('mapServiceChannelsOnly',5),(_K,6),(_L,7),('sptsServiceChannelsOnly',8),('sptsMapServiceChannelsOnly',9),('sptsFullDpmControl',10)))
_TsoutMOIPOutputMode_Type.__name__=_B
_TsoutMOIPOutputMode_Object=MibTableColumn
tsoutMOIPOutputMode=_TsoutMOIPOutputMode_Object((1,3,6,1,4,1,1429,2,2,5,34,1,1,8),_TsoutMOIPOutputMode_Type())
tsoutMOIPOutputMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tsoutMOIPOutputMode.setStatus(_A)
_TsoutStatusTable_Object=MibTable
tsoutStatusTable=_TsoutStatusTable_Object((1,3,6,1,4,1,1429,2,2,5,34,2))
if mibBuilder.loadTexts:tsoutStatusTable.setStatus(_A)
_TsoutStatusEntry_Object=MibTableRow
tsoutStatusEntry=_TsoutStatusEntry_Object((1,3,6,1,4,1,1429,2,2,5,34,2,1))
tsoutStatusEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:tsoutStatusEntry.setStatus(_A)
class _TsoutStatusID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_TsoutStatusID_Type.__name__=_B
_TsoutStatusID_Object=MibTableColumn
tsoutStatusID=_TsoutStatusID_Object((1,3,6,1,4,1,1429,2,2,5,34,2,1,1),_TsoutStatusID_Type())
tsoutStatusID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tsoutStatusID.setStatus(_A)
class _TsoutStatusInstanceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TsoutStatusInstanceName_Type.__name__=_E
_TsoutStatusInstanceName_Object=MibTableColumn
tsoutStatusInstanceName=_TsoutStatusInstanceName_Object((1,3,6,1,4,1,1429,2,2,5,34,2,1,2),_TsoutStatusInstanceName_Type())
tsoutStatusInstanceName.setMaxAccess(_D)
if mibBuilder.loadTexts:tsoutStatusInstanceName.setStatus(_A)
class _TsoutStatusRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_TsoutStatusRate_Type.__name__=_B
_TsoutStatusRate_Object=MibTableColumn
tsoutStatusRate=_TsoutStatusRate_Object((1,3,6,1,4,1,1429,2,2,5,34,2,1,3),_TsoutStatusRate_Type())
tsoutStatusRate.setMaxAccess(_D)
if mibBuilder.loadTexts:tsoutStatusRate.setStatus(_A)
class _TsoutStatusFree_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_TsoutStatusFree_Type.__name__=_B
_TsoutStatusFree_Object=MibTableColumn
tsoutStatusFree=_TsoutStatusFree_Object((1,3,6,1,4,1,1429,2,2,5,34,2,1,4),_TsoutStatusFree_Type())
tsoutStatusFree.setMaxAccess(_D)
if mibBuilder.loadTexts:tsoutStatusFree.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ciscoDSGTSOUT':ciscoDSGTSOUT,'tsoutTable':tsoutTable,'tsoutEntry':tsoutEntry,_G:tsoutID,'tsoutInstanceName':tsoutInstanceName,'tsoutOutputMode':tsoutOutputMode,'tsoutDescrambleMode':tsoutDescrambleMode,'tsoutRateControl':tsoutRateControl,'tsoutOutputRate':tsoutOutputRate,'tsoutInsertNullPkt':tsoutInsertNullPkt,'tsoutMOIPOutputMode':tsoutMOIPOutputMode,'tsoutStatusTable':tsoutStatusTable,'tsoutStatusEntry':tsoutStatusEntry,_M:tsoutStatusID,'tsoutStatusInstanceName':tsoutStatusInstanceName,'tsoutStatusRate':tsoutStatusRate,'tsoutStatusFree':tsoutStatusFree})