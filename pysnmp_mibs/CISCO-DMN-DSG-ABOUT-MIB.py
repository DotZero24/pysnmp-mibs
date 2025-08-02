_H='firmwareIdx'
_G='boardIdx'
_F='not-accessible'
_E='CISCO-DMN-DSG-ABOUT-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
ciscoDSGAbout=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,7))
if mibBuilder.loadTexts:ciscoDSGAbout.setRevisions(('2010-08-03 06:00','2010-03-22 05:00','2009-12-20 15:00'))
_AboutTable_ObjectIdentity=ObjectIdentity
aboutTable=_AboutTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,7,2))
_BoardTable_Object=MibTable
boardTable=_BoardTable_Object((1,3,6,1,4,1,1429,2,2,5,7,2,1))
if mibBuilder.loadTexts:boardTable.setStatus(_A)
_BoardEntry_Object=MibTableRow
boardEntry=_BoardEntry_Object((1,3,6,1,4,1,1429,2,2,5,7,2,1,1))
boardEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:boardEntry.setStatus(_A)
class _BoardIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BoardIdx_Type.__name__=_D
_BoardIdx_Object=MibTableColumn
boardIdx=_BoardIdx_Object((1,3,6,1,4,1,1429,2,2,5,7,2,1,1,1),_BoardIdx_Type())
boardIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:boardIdx.setStatus(_A)
class _BoardPosition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_BoardPosition_Type.__name__=_D
_BoardPosition_Object=MibTableColumn
boardPosition=_BoardPosition_Object((1,3,6,1,4,1,1429,2,2,5,7,2,1,1,2),_BoardPosition_Type())
boardPosition.setMaxAccess(_B)
if mibBuilder.loadTexts:boardPosition.setStatus(_A)
class _BoardID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_BoardID_Type.__name__=_C
_BoardID_Object=MibTableColumn
boardID=_BoardID_Object((1,3,6,1,4,1,1429,2,2,5,7,2,1,1,3),_BoardID_Type())
boardID.setMaxAccess(_B)
if mibBuilder.loadTexts:boardID.setStatus(_A)
class _BoardRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_BoardRev_Type.__name__=_C
_BoardRev_Object=MibTableColumn
boardRev=_BoardRev_Object((1,3,6,1,4,1,1429,2,2,5,7,2,1,1,4),_BoardRev_Type())
boardRev.setMaxAccess(_B)
if mibBuilder.loadTexts:boardRev.setStatus(_A)
class _BoardOptionBits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BoardOptionBits_Type.__name__=_D
_BoardOptionBits_Object=MibTableColumn
boardOptionBits=_BoardOptionBits_Object((1,3,6,1,4,1,1429,2,2,5,7,2,1,1,5),_BoardOptionBits_Type())
boardOptionBits.setMaxAccess(_B)
if mibBuilder.loadTexts:boardOptionBits.setStatus(_A)
class _BoardSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_BoardSerialNum_Type.__name__=_C
_BoardSerialNum_Object=MibTableColumn
boardSerialNum=_BoardSerialNum_Object((1,3,6,1,4,1,1429,2,2,5,7,2,1,1,6),_BoardSerialNum_Type())
boardSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:boardSerialNum.setStatus(_A)
_SwTable_Object=MibTable
swTable=_SwTable_Object((1,3,6,1,4,1,1429,2,2,5,7,2,3))
if mibBuilder.loadTexts:swTable.setStatus(_A)
_SwEntry_Object=MibTableRow
swEntry=_SwEntry_Object((1,3,6,1,4,1,1429,2,2,5,7,2,3,1))
swEntry.setIndexNames((0,_E,'swIdx'))
if mibBuilder.loadTexts:swEntry.setStatus(_A)
class _SwIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SwIdx_Type.__name__=_D
_SwIdx_Object=MibTableColumn
swIdx=_SwIdx_Object((1,3,6,1,4,1,1429,2,2,5,7,2,3,1,1),_SwIdx_Type())
swIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:swIdx.setStatus(_A)
class _SwBoardIdx_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_SwBoardIdx_Type.__name__=_C
_SwBoardIdx_Object=MibTableColumn
swBoardIdx=_SwBoardIdx_Object((1,3,6,1,4,1,1429,2,2,5,7,2,3,1,2),_SwBoardIdx_Type())
swBoardIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:swBoardIdx.setStatus(_A)
class _SwID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_SwID_Type.__name__=_C
_SwID_Object=MibTableColumn
swID=_SwID_Object((1,3,6,1,4,1,1429,2,2,5,7,2,3,1,3),_SwID_Type())
swID.setMaxAccess(_B)
if mibBuilder.loadTexts:swID.setStatus(_A)
class _SwFileIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwFileIdx_Type.__name__=_D
_SwFileIdx_Object=MibTableColumn
swFileIdx=_SwFileIdx_Object((1,3,6,1,4,1,1429,2,2,5,7,2,3,1,4),_SwFileIdx_Type())
swFileIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:swFileIdx.setStatus(_A)
class _SwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,35))
_SwVersion_Type.__name__=_C
_SwVersion_Object=MibTableColumn
swVersion=_SwVersion_Object((1,3,6,1,4,1,1429,2,2,5,7,2,3,1,5),_SwVersion_Type())
swVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:swVersion.setStatus(_A)
class _SwValidationCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,35))
_SwValidationCode_Type.__name__=_C
_SwValidationCode_Object=MibTableColumn
swValidationCode=_SwValidationCode_Object((1,3,6,1,4,1,1429,2,2,5,7,2,3,1,6),_SwValidationCode_Type())
swValidationCode.setMaxAccess(_B)
if mibBuilder.loadTexts:swValidationCode.setStatus(_A)
class _SwStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('running',1),('ready',2)))
_SwStatus_Type.__name__=_D
_SwStatus_Object=MibTableColumn
swStatus=_SwStatus_Object((1,3,6,1,4,1,1429,2,2,5,7,2,3,1,7),_SwStatus_Type())
swStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:swStatus.setStatus(_A)
class _SwCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('select',2),('erase',3)))
_SwCtrl_Type.__name__=_D
_SwCtrl_Object=MibTableColumn
swCtrl=_SwCtrl_Object((1,3,6,1,4,1,1429,2,2,5,7,2,3,1,8),_SwCtrl_Type())
swCtrl.setMaxAccess('read-write')
if mibBuilder.loadTexts:swCtrl.setStatus(_A)
_FirmwareTable_Object=MibTable
firmwareTable=_FirmwareTable_Object((1,3,6,1,4,1,1429,2,2,5,7,2,4))
if mibBuilder.loadTexts:firmwareTable.setStatus(_A)
_FirmwareEntry_Object=MibTableRow
firmwareEntry=_FirmwareEntry_Object((1,3,6,1,4,1,1429,2,2,5,7,2,4,1))
firmwareEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:firmwareEntry.setStatus(_A)
class _FirmwareIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FirmwareIdx_Type.__name__=_D
_FirmwareIdx_Object=MibTableColumn
firmwareIdx=_FirmwareIdx_Object((1,3,6,1,4,1,1429,2,2,5,7,2,4,1,1),_FirmwareIdx_Type())
firmwareIdx.setMaxAccess(_F)
if mibBuilder.loadTexts:firmwareIdx.setStatus(_A)
class _FirmwareBoardID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_FirmwareBoardID_Type.__name__=_C
_FirmwareBoardID_Object=MibTableColumn
firmwareBoardID=_FirmwareBoardID_Object((1,3,6,1,4,1,1429,2,2,5,7,2,4,1,2),_FirmwareBoardID_Type())
firmwareBoardID.setMaxAccess(_B)
if mibBuilder.loadTexts:firmwareBoardID.setStatus(_A)
class _FirmwareID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_FirmwareID_Type.__name__=_C
_FirmwareID_Object=MibTableColumn
firmwareID=_FirmwareID_Object((1,3,6,1,4,1,1429,2,2,5,7,2,4,1,3),_FirmwareID_Type())
firmwareID.setMaxAccess(_B)
if mibBuilder.loadTexts:firmwareID.setStatus(_A)
class _FirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_FirmwareVersion_Type.__name__=_C
_FirmwareVersion_Object=MibTableColumn
firmwareVersion=_FirmwareVersion_Object((1,3,6,1,4,1,1429,2,2,5,7,2,4,1,4),_FirmwareVersion_Type())
firmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:firmwareVersion.setStatus(_A)
class _FirmwareValidationCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,49))
_FirmwareValidationCode_Type.__name__=_C
_FirmwareValidationCode_Object=MibTableColumn
firmwareValidationCode=_FirmwareValidationCode_Object((1,3,6,1,4,1,1429,2,2,5,7,2,4,1,5),_FirmwareValidationCode_Type())
firmwareValidationCode.setMaxAccess(_B)
if mibBuilder.loadTexts:firmwareValidationCode.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ciscoDSGAbout':ciscoDSGAbout,'aboutTable':aboutTable,'boardTable':boardTable,'boardEntry':boardEntry,_G:boardIdx,'boardPosition':boardPosition,'boardID':boardID,'boardRev':boardRev,'boardOptionBits':boardOptionBits,'boardSerialNum':boardSerialNum,'swTable':swTable,'swEntry':swEntry,'swIdx':swIdx,'swBoardIdx':swBoardIdx,'swID':swID,'swFileIdx':swFileIdx,'swVersion':swVersion,'swValidationCode':swValidationCode,'swStatus':swStatus,'swCtrl':swCtrl,'firmwareTable':firmwareTable,'firmwareEntry':firmwareEntry,_H:firmwareIdx,'firmwareBoardID':firmwareBoardID,'firmwareID':firmwareID,'firmwareVersion':firmwareVersion,'firmwareValidationCode':firmwareValidationCode})