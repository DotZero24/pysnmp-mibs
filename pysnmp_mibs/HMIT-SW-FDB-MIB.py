_L='hmITSwFDBfdbType'
_K='hmITSwFDBfdbPort'
_J='hmITSwFDBfdbVlanId'
_I='hmITSwFDBfdbMacAddr'
_H='hmITSwFDBmacLearnPort'
_G='hmITSwFDBmacLearnVlan'
_F='DisplayString'
_E='read-only'
_D='HMIT-SW-FDB-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmITSwitchTech,=mibBuilder.importSymbols('HMIT-SMI','hmITSwitchTech')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
hmITSwFDB=ModuleIdentity((1,3,6,1,4,1,248,100,1,6,3,12))
if mibBuilder.loadTexts:hmITSwFDB.setRevisions(('2010-01-08 17:00',))
class _HmITSwFDBAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_HmITSwFDBAgingTime_Type.__name__=_B
_HmITSwFDBAgingTime_Object=MibScalar
hmITSwFDBAgingTime=_HmITSwFDBAgingTime_Object((1,3,6,1,4,1,248,100,1,6,3,12,1),_HmITSwFDBAgingTime_Type())
hmITSwFDBAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITSwFDBAgingTime.setStatus(_A)
class _HmITSwFDBSytemMacLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_HmITSwFDBSytemMacLimit_Type.__name__=_B
_HmITSwFDBSytemMacLimit_Object=MibScalar
hmITSwFDBSytemMacLimit=_HmITSwFDBSytemMacLimit_Object((1,3,6,1,4,1,248,100,1,6,3,12,2),_HmITSwFDBSytemMacLimit_Type())
hmITSwFDBSytemMacLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITSwFDBSytemMacLimit.setStatus(_A)
_HmITSwFDBVlanMacLearnTable_Object=MibTable
hmITSwFDBVlanMacLearnTable=_HmITSwFDBVlanMacLearnTable_Object((1,3,6,1,4,1,248,100,1,6,3,12,3))
if mibBuilder.loadTexts:hmITSwFDBVlanMacLearnTable.setStatus(_A)
_HmITSwFDBVlanMacLearnEntry_Object=MibTableRow
hmITSwFDBVlanMacLearnEntry=_HmITSwFDBVlanMacLearnEntry_Object((1,3,6,1,4,1,248,100,1,6,3,12,3,1))
hmITSwFDBVlanMacLearnEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hmITSwFDBVlanMacLearnEntry.setStatus(_A)
class _HmITSwFDBmacLearnVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_HmITSwFDBmacLearnVlan_Type.__name__=_B
_HmITSwFDBmacLearnVlan_Object=MibTableColumn
hmITSwFDBmacLearnVlan=_HmITSwFDBmacLearnVlan_Object((1,3,6,1,4,1,248,100,1,6,3,12,3,1,1),_HmITSwFDBmacLearnVlan_Type())
hmITSwFDBmacLearnVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:hmITSwFDBmacLearnVlan.setStatus(_A)
class _HmITSwFDBmacLearnNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_HmITSwFDBmacLearnNum_Type.__name__=_B
_HmITSwFDBmacLearnNum_Object=MibTableColumn
hmITSwFDBmacLearnNum=_HmITSwFDBmacLearnNum_Object((1,3,6,1,4,1,248,100,1,6,3,12,3,1,2),_HmITSwFDBmacLearnNum_Type())
hmITSwFDBmacLearnNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITSwFDBmacLearnNum.setStatus(_A)
_HmITSwFDBmacLearnStatus_Type=RowStatus
_HmITSwFDBmacLearnStatus_Object=MibTableColumn
hmITSwFDBmacLearnStatus=_HmITSwFDBmacLearnStatus_Object((1,3,6,1,4,1,248,100,1,6,3,12,3,1,3),_HmITSwFDBmacLearnStatus_Type())
hmITSwFDBmacLearnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITSwFDBmacLearnStatus.setStatus(_A)
_HmITSwFDBPortMacLearnTable_Object=MibTable
hmITSwFDBPortMacLearnTable=_HmITSwFDBPortMacLearnTable_Object((1,3,6,1,4,1,248,100,1,6,3,12,9))
if mibBuilder.loadTexts:hmITSwFDBPortMacLearnTable.setStatus(_A)
_HmITSwFDBPortMacLearnEntry_Object=MibTableRow
hmITSwFDBPortMacLearnEntry=_HmITSwFDBPortMacLearnEntry_Object((1,3,6,1,4,1,248,100,1,6,3,12,9,1))
hmITSwFDBPortMacLearnEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:hmITSwFDBPortMacLearnEntry.setStatus(_A)
class _HmITSwFDBmacLearnPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HmITSwFDBmacLearnPort_Type.__name__=_B
_HmITSwFDBmacLearnPort_Object=MibTableColumn
hmITSwFDBmacLearnPort=_HmITSwFDBmacLearnPort_Object((1,3,6,1,4,1,248,100,1,6,3,12,9,1,1),_HmITSwFDBmacLearnPort_Type())
hmITSwFDBmacLearnPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hmITSwFDBmacLearnPort.setStatus(_A)
class _HmITSwFDBPortmacLearnNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_HmITSwFDBPortmacLearnNum_Type.__name__=_B
_HmITSwFDBPortmacLearnNum_Object=MibTableColumn
hmITSwFDBPortmacLearnNum=_HmITSwFDBPortmacLearnNum_Object((1,3,6,1,4,1,248,100,1,6,3,12,9,1,2),_HmITSwFDBPortmacLearnNum_Type())
hmITSwFDBPortmacLearnNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITSwFDBPortmacLearnNum.setStatus(_A)
_HmITSwFDBPortmacLearnStatus_Type=RowStatus
_HmITSwFDBPortmacLearnStatus_Object=MibTableColumn
hmITSwFDBPortmacLearnStatus=_HmITSwFDBPortmacLearnStatus_Object((1,3,6,1,4,1,248,100,1,6,3,12,9,1,3),_HmITSwFDBPortmacLearnStatus_Type())
hmITSwFDBPortmacLearnStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITSwFDBPortmacLearnStatus.setStatus(_A)
_HmITSwFDBFdbTable_Object=MibTable
hmITSwFDBFdbTable=_HmITSwFDBFdbTable_Object((1,3,6,1,4,1,248,100,1,6,3,12,10))
if mibBuilder.loadTexts:hmITSwFDBFdbTable.setStatus(_A)
_HmITSwFDBFdbEntry_Object=MibTableRow
hmITSwFDBFdbEntry=_HmITSwFDBFdbEntry_Object((1,3,6,1,4,1,248,100,1,6,3,12,10,1))
hmITSwFDBFdbEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:hmITSwFDBFdbEntry.setStatus(_A)
_HmITSwFDBfdbMacAddr_Type=MacAddress
_HmITSwFDBfdbMacAddr_Object=MibTableColumn
hmITSwFDBfdbMacAddr=_HmITSwFDBfdbMacAddr_Object((1,3,6,1,4,1,248,100,1,6,3,12,10,1,1),_HmITSwFDBfdbMacAddr_Type())
hmITSwFDBfdbMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITSwFDBfdbMacAddr.setStatus(_A)
class _HmITSwFDBfdbVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HmITSwFDBfdbVlanId_Type.__name__=_B
_HmITSwFDBfdbVlanId_Object=MibTableColumn
hmITSwFDBfdbVlanId=_HmITSwFDBfdbVlanId_Object((1,3,6,1,4,1,248,100,1,6,3,12,10,1,2),_HmITSwFDBfdbVlanId_Type())
hmITSwFDBfdbVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITSwFDBfdbVlanId.setStatus(_A)
class _HmITSwFDBfdbPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HmITSwFDBfdbPort_Type.__name__=_B
_HmITSwFDBfdbPort_Object=MibTableColumn
hmITSwFDBfdbPort=_HmITSwFDBfdbPort_Object((1,3,6,1,4,1,248,100,1,6,3,12,10,1,3),_HmITSwFDBfdbPort_Type())
hmITSwFDBfdbPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITSwFDBfdbPort.setStatus(_A)
class _HmITSwFDBfdbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_HmITSwFDBfdbType_Type.__name__=_B
_HmITSwFDBfdbType_Object=MibTableColumn
hmITSwFDBfdbType=_HmITSwFDBfdbType_Object((1,3,6,1,4,1,248,100,1,6,3,12,10,1,4),_HmITSwFDBfdbType_Type())
hmITSwFDBfdbType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITSwFDBfdbType.setStatus(_A)
class _HmITSwFDBfdbState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_HmITSwFDBfdbState_Type.__name__=_B
_HmITSwFDBfdbState_Object=MibTableColumn
hmITSwFDBfdbState=_HmITSwFDBfdbState_Object((1,3,6,1,4,1,248,100,1,6,3,12,10,1,5),_HmITSwFDBfdbState_Type())
hmITSwFDBfdbState.setMaxAccess(_E)
if mibBuilder.loadTexts:hmITSwFDBfdbState.setStatus(_A)
_HmITSwFDBfdbStatus_Type=RowStatus
_HmITSwFDBfdbStatus_Object=MibTableColumn
hmITSwFDBfdbStatus=_HmITSwFDBfdbStatus_Object((1,3,6,1,4,1,248,100,1,6,3,12,10,1,6),_HmITSwFDBfdbStatus_Type())
hmITSwFDBfdbStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hmITSwFDBfdbStatus.setStatus(_A)
class _HmITSwFDBDelPortindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32768))
_HmITSwFDBDelPortindex_Type.__name__=_B
_HmITSwFDBDelPortindex_Object=MibScalar
hmITSwFDBDelPortindex=_HmITSwFDBDelPortindex_Object((1,3,6,1,4,1,248,100,1,6,3,12,13),_HmITSwFDBDelPortindex_Type())
hmITSwFDBDelPortindex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITSwFDBDelPortindex.setStatus(_A)
class _HmITSwFDBDelVlanindex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HmITSwFDBDelVlanindex_Type.__name__=_B
_HmITSwFDBDelVlanindex_Object=MibScalar
hmITSwFDBDelVlanindex=_HmITSwFDBDelVlanindex_Object((1,3,6,1,4,1,248,100,1,6,3,12,14),_HmITSwFDBDelVlanindex_Type())
hmITSwFDBDelVlanindex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITSwFDBDelVlanindex.setStatus(_A)
class _HmITSwFDBDelPortVlanindex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,10))
_HmITSwFDBDelPortVlanindex_Type.__name__=_F
_HmITSwFDBDelPortVlanindex_Object=MibScalar
hmITSwFDBDelPortVlanindex=_HmITSwFDBDelPortVlanindex_Object((1,3,6,1,4,1,248,100,1,6,3,12,15),_HmITSwFDBDelPortVlanindex_Type())
hmITSwFDBDelPortVlanindex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITSwFDBDelPortVlanindex.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hmITSwFDB':hmITSwFDB,'hmITSwFDBAgingTime':hmITSwFDBAgingTime,'hmITSwFDBSytemMacLimit':hmITSwFDBSytemMacLimit,'hmITSwFDBVlanMacLearnTable':hmITSwFDBVlanMacLearnTable,'hmITSwFDBVlanMacLearnEntry':hmITSwFDBVlanMacLearnEntry,_G:hmITSwFDBmacLearnVlan,'hmITSwFDBmacLearnNum':hmITSwFDBmacLearnNum,'hmITSwFDBmacLearnStatus':hmITSwFDBmacLearnStatus,'hmITSwFDBPortMacLearnTable':hmITSwFDBPortMacLearnTable,'hmITSwFDBPortMacLearnEntry':hmITSwFDBPortMacLearnEntry,_H:hmITSwFDBmacLearnPort,'hmITSwFDBPortmacLearnNum':hmITSwFDBPortmacLearnNum,'hmITSwFDBPortmacLearnStatus':hmITSwFDBPortmacLearnStatus,'hmITSwFDBFdbTable':hmITSwFDBFdbTable,'hmITSwFDBFdbEntry':hmITSwFDBFdbEntry,_I:hmITSwFDBfdbMacAddr,_J:hmITSwFDBfdbVlanId,_K:hmITSwFDBfdbPort,_L:hmITSwFDBfdbType,'hmITSwFDBfdbState':hmITSwFDBfdbState,'hmITSwFDBfdbStatus':hmITSwFDBfdbStatus,'hmITSwFDBDelPortindex':hmITSwFDBDelPortindex,'hmITSwFDBDelVlanindex':hmITSwFDBDelVlanindex,'hmITSwFDBDelPortVlanindex':hmITSwFDBDelPortVlanindex})