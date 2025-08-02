_K='hpnsaScsiDevLunIndex'
_J='hpnsaScsiDevTargIdIndex'
_I='hpnsaScsiDevHbaIndex'
_H='hpnsaScsiHbaIndex'
_G='hpnsaScsiAgentModuleIndex'
_F='OctetString'
_E='HPNSASCSI-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_Nm_ObjectIdentity=ObjectIdentity
nm=_Nm_ObjectIdentity((1,3,6,1,4,1,11,2))
_Hpnsa_ObjectIdentity=ObjectIdentity
hpnsa=_Hpnsa_ObjectIdentity((1,3,6,1,4,1,11,2,23))
_HpnsaScsi_ObjectIdentity=ObjectIdentity
hpnsaScsi=_HpnsaScsi_ObjectIdentity((1,3,6,1,4,1,11,2,23,14))
_HpnsaScsiMibRev_ObjectIdentity=ObjectIdentity
hpnsaScsiMibRev=_HpnsaScsiMibRev_ObjectIdentity((1,3,6,1,4,1,11,2,23,14,1))
class _HpnsaScsiMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnsaScsiMibRevMajor_Type.__name__=_C
_HpnsaScsiMibRevMajor_Object=MibScalar
hpnsaScsiMibRevMajor=_HpnsaScsiMibRevMajor_Object((1,3,6,1,4,1,11,2,23,14,1,1),_HpnsaScsiMibRevMajor_Type())
hpnsaScsiMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiMibRevMajor.setStatus(_A)
class _HpnsaScsiMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaScsiMibRevMinor_Type.__name__=_C
_HpnsaScsiMibRevMinor_Object=MibScalar
hpnsaScsiMibRevMinor=_HpnsaScsiMibRevMinor_Object((1,3,6,1,4,1,11,2,23,14,1,2),_HpnsaScsiMibRevMinor_Type())
hpnsaScsiMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiMibRevMinor.setStatus(_A)
_HpnsaScsiAgent_ObjectIdentity=ObjectIdentity
hpnsaScsiAgent=_HpnsaScsiAgent_ObjectIdentity((1,3,6,1,4,1,11,2,23,14,2))
_HpnsaScsiAgentModuleTable_Object=MibTable
hpnsaScsiAgentModuleTable=_HpnsaScsiAgentModuleTable_Object((1,3,6,1,4,1,11,2,23,14,2,1))
if mibBuilder.loadTexts:hpnsaScsiAgentModuleTable.setStatus(_A)
_HpnsaScsiAgentModuleEntry_Object=MibTableRow
hpnsaScsiAgentModuleEntry=_HpnsaScsiAgentModuleEntry_Object((1,3,6,1,4,1,11,2,23,14,2,1,1))
hpnsaScsiAgentModuleEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:hpnsaScsiAgentModuleEntry.setStatus(_A)
class _HpnsaScsiAgentModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaScsiAgentModuleIndex_Type.__name__=_C
_HpnsaScsiAgentModuleIndex_Object=MibTableColumn
hpnsaScsiAgentModuleIndex=_HpnsaScsiAgentModuleIndex_Object((1,3,6,1,4,1,11,2,23,14,2,1,1,1),_HpnsaScsiAgentModuleIndex_Type())
hpnsaScsiAgentModuleIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiAgentModuleIndex.setStatus(_A)
class _HpnsaScsiAgentModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnsaScsiAgentModuleName_Type.__name__=_D
_HpnsaScsiAgentModuleName_Object=MibTableColumn
hpnsaScsiAgentModuleName=_HpnsaScsiAgentModuleName_Object((1,3,6,1,4,1,11,2,23,14,2,1,1,2),_HpnsaScsiAgentModuleName_Type())
hpnsaScsiAgentModuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiAgentModuleName.setStatus(_A)
class _HpnsaScsiAgentModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpnsaScsiAgentModuleVersion_Type.__name__=_D
_HpnsaScsiAgentModuleVersion_Object=MibTableColumn
hpnsaScsiAgentModuleVersion=_HpnsaScsiAgentModuleVersion_Object((1,3,6,1,4,1,11,2,23,14,2,1,1,3),_HpnsaScsiAgentModuleVersion_Type())
hpnsaScsiAgentModuleVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiAgentModuleVersion.setStatus(_A)
class _HpnsaScsiAgentModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_HpnsaScsiAgentModuleDate_Type.__name__=_F
_HpnsaScsiAgentModuleDate_Object=MibTableColumn
hpnsaScsiAgentModuleDate=_HpnsaScsiAgentModuleDate_Object((1,3,6,1,4,1,11,2,23,14,2,1,1,4),_HpnsaScsiAgentModuleDate_Type())
hpnsaScsiAgentModuleDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiAgentModuleDate.setStatus(_A)
_HpnsaScsiHba_ObjectIdentity=ObjectIdentity
hpnsaScsiHba=_HpnsaScsiHba_ObjectIdentity((1,3,6,1,4,1,11,2,23,14,3))
_HpnsaScsiHbaTable_Object=MibTable
hpnsaScsiHbaTable=_HpnsaScsiHbaTable_Object((1,3,6,1,4,1,11,2,23,14,3,1))
if mibBuilder.loadTexts:hpnsaScsiHbaTable.setStatus(_A)
_HpnsaScsiHbaEntry_Object=MibTableRow
hpnsaScsiHbaEntry=_HpnsaScsiHbaEntry_Object((1,3,6,1,4,1,11,2,23,14,3,1,1))
hpnsaScsiHbaEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:hpnsaScsiHbaEntry.setStatus(_A)
class _HpnsaScsiHbaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaScsiHbaIndex_Type.__name__=_C
_HpnsaScsiHbaIndex_Object=MibTableColumn
hpnsaScsiHbaIndex=_HpnsaScsiHbaIndex_Object((1,3,6,1,4,1,11,2,23,14,3,1,1,1),_HpnsaScsiHbaIndex_Type())
hpnsaScsiHbaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiHbaIndex.setStatus(_A)
class _HpnsaScsiHbaTargetId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnsaScsiHbaTargetId_Type.__name__=_C
_HpnsaScsiHbaTargetId_Object=MibTableColumn
hpnsaScsiHbaTargetId=_HpnsaScsiHbaTargetId_Object((1,3,6,1,4,1,11,2,23,14,3,1,1,2),_HpnsaScsiHbaTargetId_Type())
hpnsaScsiHbaTargetId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiHbaTargetId.setStatus(_A)
class _HpnsaScsiHbaManagerId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_HpnsaScsiHbaManagerId_Type.__name__=_D
_HpnsaScsiHbaManagerId_Object=MibTableColumn
hpnsaScsiHbaManagerId=_HpnsaScsiHbaManagerId_Object((1,3,6,1,4,1,11,2,23,14,3,1,1,3),_HpnsaScsiHbaManagerId_Type())
hpnsaScsiHbaManagerId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiHbaManagerId.setStatus(_A)
class _HpnsaScsiHbaHostAdapterId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_HpnsaScsiHbaHostAdapterId_Type.__name__=_D
_HpnsaScsiHbaHostAdapterId_Object=MibTableColumn
hpnsaScsiHbaHostAdapterId=_HpnsaScsiHbaHostAdapterId_Object((1,3,6,1,4,1,11,2,23,14,3,1,1,4),_HpnsaScsiHbaHostAdapterId_Type())
hpnsaScsiHbaHostAdapterId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiHbaHostAdapterId.setStatus(_A)
_HpnsaScsiDev_ObjectIdentity=ObjectIdentity
hpnsaScsiDev=_HpnsaScsiDev_ObjectIdentity((1,3,6,1,4,1,11,2,23,14,4))
_HpnsaScsiDevTable_Object=MibTable
hpnsaScsiDevTable=_HpnsaScsiDevTable_Object((1,3,6,1,4,1,11,2,23,14,4,1))
if mibBuilder.loadTexts:hpnsaScsiDevTable.setStatus(_A)
_HpnsaScsiDevEntry_Object=MibTableRow
hpnsaScsiDevEntry=_HpnsaScsiDevEntry_Object((1,3,6,1,4,1,11,2,23,14,4,1,1))
hpnsaScsiDevEntry.setIndexNames((0,_E,_I),(0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:hpnsaScsiDevEntry.setStatus(_A)
class _HpnsaScsiDevHbaIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnsaScsiDevHbaIndex_Type.__name__=_C
_HpnsaScsiDevHbaIndex_Object=MibTableColumn
hpnsaScsiDevHbaIndex=_HpnsaScsiDevHbaIndex_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,1),_HpnsaScsiDevHbaIndex_Type())
hpnsaScsiDevHbaIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevHbaIndex.setStatus(_A)
class _HpnsaScsiDevTargIdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnsaScsiDevTargIdIndex_Type.__name__=_C
_HpnsaScsiDevTargIdIndex_Object=MibTableColumn
hpnsaScsiDevTargIdIndex=_HpnsaScsiDevTargIdIndex_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,2),_HpnsaScsiDevTargIdIndex_Type())
hpnsaScsiDevTargIdIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevTargIdIndex.setStatus(_A)
class _HpnsaScsiDevLunIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnsaScsiDevLunIndex_Type.__name__=_C
_HpnsaScsiDevLunIndex_Object=MibTableColumn
hpnsaScsiDevLunIndex=_HpnsaScsiDevLunIndex_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,3),_HpnsaScsiDevLunIndex_Type())
hpnsaScsiDevLunIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevLunIndex.setStatus(_A)
class _HpnsaScsiDevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_HpnsaScsiDevType_Type.__name__=_C
_HpnsaScsiDevType_Object=MibTableColumn
hpnsaScsiDevType=_HpnsaScsiDevType_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,4),_HpnsaScsiDevType_Type())
hpnsaScsiDevType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevType.setStatus(_A)
class _HpnsaScsiDevRmb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_HpnsaScsiDevRmb_Type.__name__=_C
_HpnsaScsiDevRmb_Object=MibTableColumn
hpnsaScsiDevRmb=_HpnsaScsiDevRmb_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,5),_HpnsaScsiDevRmb_Type())
hpnsaScsiDevRmb.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevRmb.setStatus(_A)
class _HpnsaScsiDevAnsiVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnsaScsiDevAnsiVer_Type.__name__=_C
_HpnsaScsiDevAnsiVer_Object=MibTableColumn
hpnsaScsiDevAnsiVer=_HpnsaScsiDevAnsiVer_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,6),_HpnsaScsiDevAnsiVer_Type())
hpnsaScsiDevAnsiVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevAnsiVer.setStatus(_A)
class _HpnsaScsiDevEcmaVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnsaScsiDevEcmaVer_Type.__name__=_C
_HpnsaScsiDevEcmaVer_Object=MibTableColumn
hpnsaScsiDevEcmaVer=_HpnsaScsiDevEcmaVer_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,7),_HpnsaScsiDevEcmaVer_Type())
hpnsaScsiDevEcmaVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevEcmaVer.setStatus(_A)
class _HpnsaScsiDevIsoVer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_HpnsaScsiDevIsoVer_Type.__name__=_C
_HpnsaScsiDevIsoVer_Object=MibTableColumn
hpnsaScsiDevIsoVer=_HpnsaScsiDevIsoVer_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,8),_HpnsaScsiDevIsoVer_Type())
hpnsaScsiDevIsoVer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevIsoVer.setStatus(_A)
class _HpnsaScsiDevVendorId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HpnsaScsiDevVendorId_Type.__name__=_D
_HpnsaScsiDevVendorId_Object=MibTableColumn
hpnsaScsiDevVendorId=_HpnsaScsiDevVendorId_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,9),_HpnsaScsiDevVendorId_Type())
hpnsaScsiDevVendorId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevVendorId.setStatus(_A)
class _HpnsaScsiDevProductId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HpnsaScsiDevProductId_Type.__name__=_D
_HpnsaScsiDevProductId_Object=MibTableColumn
hpnsaScsiDevProductId=_HpnsaScsiDevProductId_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,10),_HpnsaScsiDevProductId_Type())
hpnsaScsiDevProductId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevProductId.setStatus(_A)
class _HpnsaScsiDevProductRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_HpnsaScsiDevProductRev_Type.__name__=_D
_HpnsaScsiDevProductRev_Object=MibTableColumn
hpnsaScsiDevProductRev=_HpnsaScsiDevProductRev_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,11),_HpnsaScsiDevProductRev_Type())
hpnsaScsiDevProductRev.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevProductRev.setStatus(_A)
_HpnsaScsiDevLogicalBlocks_Type=Integer32
_HpnsaScsiDevLogicalBlocks_Object=MibTableColumn
hpnsaScsiDevLogicalBlocks=_HpnsaScsiDevLogicalBlocks_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,12),_HpnsaScsiDevLogicalBlocks_Type())
hpnsaScsiDevLogicalBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevLogicalBlocks.setStatus(_A)
_HpnsaScsiDevBlockLength_Type=Integer32
_HpnsaScsiDevBlockLength_Object=MibTableColumn
hpnsaScsiDevBlockLength=_HpnsaScsiDevBlockLength_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,13),_HpnsaScsiDevBlockLength_Type())
hpnsaScsiDevBlockLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevBlockLength.setStatus(_A)
class _HpnsaScsiDevCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnsaScsiDevCapacity_Type.__name__=_C
_HpnsaScsiDevCapacity_Object=MibTableColumn
hpnsaScsiDevCapacity=_HpnsaScsiDevCapacity_Object((1,3,6,1,4,1,11,2,23,14,4,1,1,14),_HpnsaScsiDevCapacity_Type())
hpnsaScsiDevCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnsaScsiDevCapacity.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hp':hp,'nm':nm,'hpnsa':hpnsa,'hpnsaScsi':hpnsaScsi,'hpnsaScsiMibRev':hpnsaScsiMibRev,'hpnsaScsiMibRevMajor':hpnsaScsiMibRevMajor,'hpnsaScsiMibRevMinor':hpnsaScsiMibRevMinor,'hpnsaScsiAgent':hpnsaScsiAgent,'hpnsaScsiAgentModuleTable':hpnsaScsiAgentModuleTable,'hpnsaScsiAgentModuleEntry':hpnsaScsiAgentModuleEntry,_G:hpnsaScsiAgentModuleIndex,'hpnsaScsiAgentModuleName':hpnsaScsiAgentModuleName,'hpnsaScsiAgentModuleVersion':hpnsaScsiAgentModuleVersion,'hpnsaScsiAgentModuleDate':hpnsaScsiAgentModuleDate,'hpnsaScsiHba':hpnsaScsiHba,'hpnsaScsiHbaTable':hpnsaScsiHbaTable,'hpnsaScsiHbaEntry':hpnsaScsiHbaEntry,_H:hpnsaScsiHbaIndex,'hpnsaScsiHbaTargetId':hpnsaScsiHbaTargetId,'hpnsaScsiHbaManagerId':hpnsaScsiHbaManagerId,'hpnsaScsiHbaHostAdapterId':hpnsaScsiHbaHostAdapterId,'hpnsaScsiDev':hpnsaScsiDev,'hpnsaScsiDevTable':hpnsaScsiDevTable,'hpnsaScsiDevEntry':hpnsaScsiDevEntry,_I:hpnsaScsiDevHbaIndex,_J:hpnsaScsiDevTargIdIndex,_K:hpnsaScsiDevLunIndex,'hpnsaScsiDevType':hpnsaScsiDevType,'hpnsaScsiDevRmb':hpnsaScsiDevRmb,'hpnsaScsiDevAnsiVer':hpnsaScsiDevAnsiVer,'hpnsaScsiDevEcmaVer':hpnsaScsiDevEcmaVer,'hpnsaScsiDevIsoVer':hpnsaScsiDevIsoVer,'hpnsaScsiDevVendorId':hpnsaScsiDevVendorId,'hpnsaScsiDevProductId':hpnsaScsiDevProductId,'hpnsaScsiDevProductRev':hpnsaScsiDevProductRev,'hpnsaScsiDevLogicalBlocks':hpnsaScsiDevLogicalBlocks,'hpnsaScsiDevBlockLength':hpnsaScsiDevBlockLength,'hpnsaScsiDevCapacity':hpnsaScsiDevCapacity})