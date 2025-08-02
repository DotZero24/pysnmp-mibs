_M='flashEntries'
_L='OLD-CISCO-FLASH-MIB'
_K='noOpAfterPowerOn'
_J='bufferAllocationFailure'
_I='flashOpenFailure'
_H='flashReadOnly'
_G='flashOpFailure'
_F='flashOpSuccess'
_E='flashOpInProgress'
_D='write-only'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
local,=mibBuilder.importSymbols('CISCO-SMI','local')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Lflash_ObjectIdentity=ObjectIdentity
lflash=_Lflash_ObjectIdentity((1,3,6,1,4,1,9,2,10))
_FlashSize_Type=Integer32
_FlashSize_Object=MibScalar
flashSize=_FlashSize_Object((1,3,6,1,4,1,9,2,10,1),_FlashSize_Type())
flashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:flashSize.setStatus(_A)
_FlashFree_Type=Integer32
_FlashFree_Object=MibScalar
flashFree=_FlashFree_Object((1,3,6,1,4,1,9,2,10,2),_FlashFree_Type())
flashFree.setMaxAccess(_B)
if mibBuilder.loadTexts:flashFree.setStatus(_A)
_FlashController_Type=DisplayString
_FlashController_Object=MibScalar
flashController=_FlashController_Object((1,3,6,1,4,1,9,2,10,3),_FlashController_Type())
flashController.setMaxAccess(_B)
if mibBuilder.loadTexts:flashController.setStatus(_A)
_FlashCard_Type=DisplayString
_FlashCard_Object=MibScalar
flashCard=_FlashCard_Object((1,3,6,1,4,1,9,2,10,4),_FlashCard_Type())
flashCard.setMaxAccess(_B)
if mibBuilder.loadTexts:flashCard.setStatus(_A)
class _FlashVPP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('installed',1),('missing',2)))
_FlashVPP_Type.__name__=_C
_FlashVPP_Object=MibScalar
flashVPP=_FlashVPP_Object((1,3,6,1,4,1,9,2,10,5),_FlashVPP_Type())
flashVPP.setMaxAccess(_B)
if mibBuilder.loadTexts:flashVPP.setStatus(_A)
_FlashErase_Type=Integer32
_FlashErase_Object=MibScalar
flashErase=_FlashErase_Object((1,3,6,1,4,1,9,2,10,6),_FlashErase_Type())
flashErase.setMaxAccess(_D)
if mibBuilder.loadTexts:flashErase.setStatus(_A)
_FlashEraseTime_Type=TimeTicks
_FlashEraseTime_Object=MibScalar
flashEraseTime=_FlashEraseTime_Object((1,3,6,1,4,1,9,2,10,7),_FlashEraseTime_Type())
flashEraseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:flashEraseTime.setStatus(_A)
class _FlashEraseStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_K,7)))
_FlashEraseStatus_Type.__name__=_C
_FlashEraseStatus_Object=MibScalar
flashEraseStatus=_FlashEraseStatus_Object((1,3,6,1,4,1,9,2,10,8),_FlashEraseStatus_Type())
flashEraseStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:flashEraseStatus.setStatus(_A)
_FlashToNet_Type=DisplayString
_FlashToNet_Object=MibScalar
flashToNet=_FlashToNet_Object((1,3,6,1,4,1,9,2,10,9),_FlashToNet_Type())
flashToNet.setMaxAccess(_D)
if mibBuilder.loadTexts:flashToNet.setStatus(_A)
_FlashToNetTime_Type=TimeTicks
_FlashToNetTime_Object=MibScalar
flashToNetTime=_FlashToNetTime_Object((1,3,6,1,4,1,9,2,10,10),_FlashToNetTime_Type())
flashToNetTime.setMaxAccess(_B)
if mibBuilder.loadTexts:flashToNetTime.setStatus(_A)
class _FlashToNetStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_K,7)))
_FlashToNetStatus_Type.__name__=_C
_FlashToNetStatus_Object=MibScalar
flashToNetStatus=_FlashToNetStatus_Object((1,3,6,1,4,1,9,2,10,11),_FlashToNetStatus_Type())
flashToNetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:flashToNetStatus.setStatus(_A)
_NetToFlash_Type=DisplayString
_NetToFlash_Object=MibScalar
netToFlash=_NetToFlash_Object((1,3,6,1,4,1,9,2,10,12),_NetToFlash_Type())
netToFlash.setMaxAccess(_D)
if mibBuilder.loadTexts:netToFlash.setStatus(_A)
_NetToFlashTime_Type=TimeTicks
_NetToFlashTime_Object=MibScalar
netToFlashTime=_NetToFlashTime_Object((1,3,6,1,4,1,9,2,10,13),_NetToFlashTime_Type())
netToFlashTime.setMaxAccess(_B)
if mibBuilder.loadTexts:netToFlashTime.setStatus(_A)
class _NetToFlashStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_K,7)))
_NetToFlashStatus_Type.__name__=_C
_NetToFlashStatus_Object=MibScalar
netToFlashStatus=_NetToFlashStatus_Object((1,3,6,1,4,1,9,2,10,14),_NetToFlashStatus_Type())
netToFlashStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:netToFlashStatus.setStatus(_A)
class _FlashStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('busy',1),('available',2)))
_FlashStatus_Type.__name__=_C
_FlashStatus_Object=MibScalar
flashStatus=_FlashStatus_Object((1,3,6,1,4,1,9,2,10,15),_FlashStatus_Type())
flashStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:flashStatus.setStatus(_A)
_FlashEntries_Type=Integer32
_FlashEntries_Object=MibScalar
flashEntries=_FlashEntries_Object((1,3,6,1,4,1,9,2,10,16),_FlashEntries_Type())
flashEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:flashEntries.setStatus(_A)
_LflashFileDirTable_Object=MibTable
lflashFileDirTable=_LflashFileDirTable_Object((1,3,6,1,4,1,9,2,10,17))
if mibBuilder.loadTexts:lflashFileDirTable.setStatus(_A)
_LflashFileDirEntry_Object=MibTableRow
lflashFileDirEntry=_LflashFileDirEntry_Object((1,3,6,1,4,1,9,2,10,17,1))
lflashFileDirEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:lflashFileDirEntry.setStatus(_A)
_FlashDirName_Type=DisplayString
_FlashDirName_Object=MibTableColumn
flashDirName=_FlashDirName_Object((1,3,6,1,4,1,9,2,10,17,1,1),_FlashDirName_Type())
flashDirName.setMaxAccess(_B)
if mibBuilder.loadTexts:flashDirName.setStatus(_A)
_FlashDirSize_Type=Integer32
_FlashDirSize_Object=MibTableColumn
flashDirSize=_FlashDirSize_Object((1,3,6,1,4,1,9,2,10,17,1,2),_FlashDirSize_Type())
flashDirSize.setMaxAccess(_B)
if mibBuilder.loadTexts:flashDirSize.setStatus(_A)
class _FlashDirStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('deleted',2)))
_FlashDirStatus_Type.__name__=_C
_FlashDirStatus_Object=MibTableColumn
flashDirStatus=_FlashDirStatus_Object((1,3,6,1,4,1,9,2,10,17,1,3),_FlashDirStatus_Type())
flashDirStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:flashDirStatus.setStatus(_A)
mibBuilder.exportSymbols(_L,**{'lflash':lflash,'flashSize':flashSize,'flashFree':flashFree,'flashController':flashController,'flashCard':flashCard,'flashVPP':flashVPP,'flashErase':flashErase,'flashEraseTime':flashEraseTime,'flashEraseStatus':flashEraseStatus,'flashToNet':flashToNet,'flashToNetTime':flashToNetTime,'flashToNetStatus':flashToNetStatus,'netToFlash':netToFlash,'netToFlashTime':netToFlashTime,'netToFlashStatus':netToFlashStatus,'flashStatus':flashStatus,_M:flashEntries,'lflashFileDirTable':lflashFileDirTable,'lflashFileDirEntry':lflashFileDirEntry,'flashDirName':flashDirName,'flashDirSize':flashDirSize,'flashDirStatus':flashDirStatus})