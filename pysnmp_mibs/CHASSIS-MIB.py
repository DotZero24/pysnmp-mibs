_K='nnchassisInfoSlotSubSlotIndex'
_J='hotswap'
_I='admindown'
_H='operdown'
_G='normal'
_F='nnSFPStatusStr'
_E='Integer32'
_D='CHASSIS-MIB'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntEnterpriseDataTasmanMgmt,=mibBuilder.importSymbols('NT-ENTERPRISE-DATA-MIB','ntEnterpriseDataTasmanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
nnchassisMib=ModuleIdentity((1,3,6,1,4,1,562,73,1,1,1,2))
if mibBuilder.loadTexts:nnchassisMib.setRevisions(('1900-01-27 00:00',))
class _NnchassisModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NnchassisModel_Type.__name__=_C
_NnchassisModel_Object=MibScalar
nnchassisModel=_NnchassisModel_Object((1,3,6,1,4,1,562,73,1,1,1,2,1),_NnchassisModel_Type())
nnchassisModel.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisModel.setStatus(_A)
class _NnchassisOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4),('boot',5),('other',6)))
_NnchassisOperStatus_Type.__name__=_E
_NnchassisOperStatus_Object=MibScalar
nnchassisOperStatus=_NnchassisOperStatus_Object((1,3,6,1,4,1,562,73,1,1,1,2,2),_NnchassisOperStatus_Type())
nnchassisOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisOperStatus.setStatus(_A)
class _NnchassisSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NnchassisSerialNumber_Type.__name__=_C
_NnchassisSerialNumber_Object=MibScalar
nnchassisSerialNumber=_NnchassisSerialNumber_Object((1,3,6,1,4,1,562,73,1,1,1,2,3),_NnchassisSerialNumber_Type())
nnchassisSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisSerialNumber.setStatus(_A)
_NnchassisRev_Type=DisplayString
_NnchassisRev_Object=MibScalar
nnchassisRev=_NnchassisRev_Object((1,3,6,1,4,1,562,73,1,1,1,2,4),_NnchassisRev_Type())
nnchassisRev.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisRev.setStatus(_A)
_NnchassisInfoTable_Object=MibTable
nnchassisInfoTable=_NnchassisInfoTable_Object((1,3,6,1,4,1,562,73,1,1,1,2,5))
if mibBuilder.loadTexts:nnchassisInfoTable.setStatus(_A)
_NnchassisInfoEntry_Object=MibTableRow
nnchassisInfoEntry=_NnchassisInfoEntry_Object((1,3,6,1,4,1,562,73,1,1,1,2,5,1))
nnchassisInfoEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:nnchassisInfoEntry.setStatus(_A)
_NnchassisInfoSlotSubSlotIndex_Type=Integer32
_NnchassisInfoSlotSubSlotIndex_Object=MibTableColumn
nnchassisInfoSlotSubSlotIndex=_NnchassisInfoSlotSubSlotIndex_Object((1,3,6,1,4,1,562,73,1,1,1,2,5,1,1),_NnchassisInfoSlotSubSlotIndex_Type())
nnchassisInfoSlotSubSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisInfoSlotSubSlotIndex.setStatus(_A)
class _NnchassisInfoSlotSubSlotString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NnchassisInfoSlotSubSlotString_Type.__name__=_C
_NnchassisInfoSlotSubSlotString_Object=MibTableColumn
nnchassisInfoSlotSubSlotString=_NnchassisInfoSlotSubSlotString_Object((1,3,6,1,4,1,562,73,1,1,1,2,5,1,2),_NnchassisInfoSlotSubSlotString_Type())
nnchassisInfoSlotSubSlotString.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisInfoSlotSubSlotString.setStatus(_A)
class _NnchassisInfoCardType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NnchassisInfoCardType_Type.__name__=_C
_NnchassisInfoCardType_Object=MibTableColumn
nnchassisInfoCardType=_NnchassisInfoCardType_Object((1,3,6,1,4,1,562,73,1,1,1,2,5,1,3),_NnchassisInfoCardType_Type())
nnchassisInfoCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisInfoCardType.setStatus(_A)
class _NnchassisInfoCardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('empty',1),(_H,2),(_I,3),(_J,4),(_G,5),('unknown',6),('other',7)))
_NnchassisInfoCardStatus_Type.__name__=_E
_NnchassisInfoCardStatus_Object=MibTableColumn
nnchassisInfoCardStatus=_NnchassisInfoCardStatus_Object((1,3,6,1,4,1,562,73,1,1,1,2,5,1,4),_NnchassisInfoCardStatus_Type())
nnchassisInfoCardStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisInfoCardStatus.setStatus(_A)
class _NnchassisInfoModelNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NnchassisInfoModelNumber_Type.__name__=_C
_NnchassisInfoModelNumber_Object=MibTableColumn
nnchassisInfoModelNumber=_NnchassisInfoModelNumber_Object((1,3,6,1,4,1,562,73,1,1,1,2,5,1,5),_NnchassisInfoModelNumber_Type())
nnchassisInfoModelNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisInfoModelNumber.setStatus(_A)
class _NnchassisInfoSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_NnchassisInfoSerialNumber_Type.__name__=_C
_NnchassisInfoSerialNumber_Object=MibTableColumn
nnchassisInfoSerialNumber=_NnchassisInfoSerialNumber_Object((1,3,6,1,4,1,562,73,1,1,1,2,5,1,6),_NnchassisInfoSerialNumber_Type())
nnchassisInfoSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisInfoSerialNumber.setStatus(_A)
_NnchassisInfoFPGARev_Type=DisplayString
_NnchassisInfoFPGARev_Object=MibTableColumn
nnchassisInfoFPGARev=_NnchassisInfoFPGARev_Object((1,3,6,1,4,1,562,73,1,1,1,2,5,1,7),_NnchassisInfoFPGARev_Type())
nnchassisInfoFPGARev.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisInfoFPGARev.setStatus(_A)
_NnchassisInfoFPGAEngRev_Type=DisplayString
_NnchassisInfoFPGAEngRev_Object=MibTableColumn
nnchassisInfoFPGAEngRev=_NnchassisInfoFPGAEngRev_Object((1,3,6,1,4,1,562,73,1,1,1,2,5,1,8),_NnchassisInfoFPGAEngRev_Type())
nnchassisInfoFPGAEngRev.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisInfoFPGAEngRev.setStatus(_A)
_NnchassisInfoCPLDRev_Type=DisplayString
_NnchassisInfoCPLDRev_Object=MibTableColumn
nnchassisInfoCPLDRev=_NnchassisInfoCPLDRev_Object((1,3,6,1,4,1,562,73,1,1,1,2,5,1,9),_NnchassisInfoCPLDRev_Type())
nnchassisInfoCPLDRev.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisInfoCPLDRev.setStatus(_A)
_NnchassisInfoCPLDEngRev_Type=DisplayString
_NnchassisInfoCPLDEngRev_Object=MibTableColumn
nnchassisInfoCPLDEngRev=_NnchassisInfoCPLDEngRev_Object((1,3,6,1,4,1,562,73,1,1,1,2,5,1,10),_NnchassisInfoCPLDEngRev_Type())
nnchassisInfoCPLDEngRev.setMaxAccess(_B)
if mibBuilder.loadTexts:nnchassisInfoCPLDEngRev.setStatus(_A)
_NnSFPTraps_ObjectIdentity=ObjectIdentity
nnSFPTraps=_NnSFPTraps_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,2,6))
_NnSFPNotifications_ObjectIdentity=ObjectIdentity
nnSFPNotifications=_NnSFPNotifications_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,2,6,0))
_NnSFPTrapVariables_ObjectIdentity=ObjectIdentity
nnSFPTrapVariables=_NnSFPTrapVariables_ObjectIdentity((1,3,6,1,4,1,562,73,1,1,1,2,6,1))
class _NnSFPStatusStr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_NnSFPStatusStr_Type.__name__=_C
_NnSFPStatusStr_Object=MibScalar
nnSFPStatusStr=_NnSFPStatusStr_Object((1,3,6,1,4,1,562,73,1,1,1,2,6,1,1),_NnSFPStatusStr_Type())
nnSFPStatusStr.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:nnSFPStatusStr.setStatus(_A)
nnSFPUpTrap=NotificationType((1,3,6,1,4,1,562,73,1,1,1,2,6,0,1))
nnSFPUpTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:nnSFPUpTrap.setStatus(_A)
nnSFPDownTrap=NotificationType((1,3,6,1,4,1,562,73,1,1,1,2,6,0,2))
nnSFPDownTrap.setObjects((_D,_F))
if mibBuilder.loadTexts:nnSFPDownTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nnchassisMib':nnchassisMib,'nnchassisModel':nnchassisModel,'nnchassisOperStatus':nnchassisOperStatus,'nnchassisSerialNumber':nnchassisSerialNumber,'nnchassisRev':nnchassisRev,'nnchassisInfoTable':nnchassisInfoTable,'nnchassisInfoEntry':nnchassisInfoEntry,_K:nnchassisInfoSlotSubSlotIndex,'nnchassisInfoSlotSubSlotString':nnchassisInfoSlotSubSlotString,'nnchassisInfoCardType':nnchassisInfoCardType,'nnchassisInfoCardStatus':nnchassisInfoCardStatus,'nnchassisInfoModelNumber':nnchassisInfoModelNumber,'nnchassisInfoSerialNumber':nnchassisInfoSerialNumber,'nnchassisInfoFPGARev':nnchassisInfoFPGARev,'nnchassisInfoFPGAEngRev':nnchassisInfoFPGAEngRev,'nnchassisInfoCPLDRev':nnchassisInfoCPLDRev,'nnchassisInfoCPLDEngRev':nnchassisInfoCPLDEngRev,'nnSFPTraps':nnSFPTraps,'nnSFPNotifications':nnSFPNotifications,'nnSFPUpTrap':nnSFPUpTrap,'nnSFPDownTrap':nnSFPDownTrap,'nnSFPTrapVariables':nnSFPTrapVariables,_F:nnSFPStatusStr})