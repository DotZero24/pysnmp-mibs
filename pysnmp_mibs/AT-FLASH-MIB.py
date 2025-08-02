_P='flashVerifyFailure'
_O='flashCompactFailure'
_N='flashEraseFailure'
_M='flashCheckFailure'
_L='flashDeleteFailure'
_K='flashPutFailure'
_J='flashCreateFailure'
_I='flashWriteFailure'
_H='flashCompleteFailure'
_G='flashCloseFailure'
_F='flashReadFailure'
_E='flashOpenFailure'
_D='flashGetFailure'
_C='read-only'
_B='AT-FLASH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB','DisplayStringUnsized','modules')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
flash=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,31))
if mibBuilder.loadTexts:flash.setRevisions(('2006-06-28 12:22',))
_FlashTrap_ObjectIdentity=ObjectIdentity
flashTrap=_FlashTrap_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,31,0))
_FlashGetFailure_Type=Integer32
_FlashGetFailure_Object=MibScalar
flashGetFailure=_FlashGetFailure_Object((1,3,6,1,4,1,207,8,4,4,4,31,1),_FlashGetFailure_Type())
flashGetFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:flashGetFailure.setStatus(_A)
_FlashOpenFailure_Type=Integer32
_FlashOpenFailure_Object=MibScalar
flashOpenFailure=_FlashOpenFailure_Object((1,3,6,1,4,1,207,8,4,4,4,31,2),_FlashOpenFailure_Type())
flashOpenFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:flashOpenFailure.setStatus(_A)
_FlashReadFailure_Type=Integer32
_FlashReadFailure_Object=MibScalar
flashReadFailure=_FlashReadFailure_Object((1,3,6,1,4,1,207,8,4,4,4,31,3),_FlashReadFailure_Type())
flashReadFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:flashReadFailure.setStatus(_A)
_FlashCloseFailure_Type=Integer32
_FlashCloseFailure_Object=MibScalar
flashCloseFailure=_FlashCloseFailure_Object((1,3,6,1,4,1,207,8,4,4,4,31,4),_FlashCloseFailure_Type())
flashCloseFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCloseFailure.setStatus(_A)
_FlashCompleteFailure_Type=Integer32
_FlashCompleteFailure_Object=MibScalar
flashCompleteFailure=_FlashCompleteFailure_Object((1,3,6,1,4,1,207,8,4,4,4,31,5),_FlashCompleteFailure_Type())
flashCompleteFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCompleteFailure.setStatus(_A)
_FlashWriteFailure_Type=Integer32
_FlashWriteFailure_Object=MibScalar
flashWriteFailure=_FlashWriteFailure_Object((1,3,6,1,4,1,207,8,4,4,4,31,6),_FlashWriteFailure_Type())
flashWriteFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:flashWriteFailure.setStatus(_A)
_FlashCreateFailure_Type=Integer32
_FlashCreateFailure_Object=MibScalar
flashCreateFailure=_FlashCreateFailure_Object((1,3,6,1,4,1,207,8,4,4,4,31,7),_FlashCreateFailure_Type())
flashCreateFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCreateFailure.setStatus(_A)
_FlashPutFailure_Type=Integer32
_FlashPutFailure_Object=MibScalar
flashPutFailure=_FlashPutFailure_Object((1,3,6,1,4,1,207,8,4,4,4,31,8),_FlashPutFailure_Type())
flashPutFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:flashPutFailure.setStatus(_A)
_FlashDeleteFailure_Type=Integer32
_FlashDeleteFailure_Object=MibScalar
flashDeleteFailure=_FlashDeleteFailure_Object((1,3,6,1,4,1,207,8,4,4,4,31,9),_FlashDeleteFailure_Type())
flashDeleteFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:flashDeleteFailure.setStatus(_A)
_FlashCheckFailure_Type=Integer32
_FlashCheckFailure_Object=MibScalar
flashCheckFailure=_FlashCheckFailure_Object((1,3,6,1,4,1,207,8,4,4,4,31,10),_FlashCheckFailure_Type())
flashCheckFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCheckFailure.setStatus(_A)
_FlashEraseFailure_Type=Integer32
_FlashEraseFailure_Object=MibScalar
flashEraseFailure=_FlashEraseFailure_Object((1,3,6,1,4,1,207,8,4,4,4,31,11),_FlashEraseFailure_Type())
flashEraseFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:flashEraseFailure.setStatus(_A)
_FlashCompactFailure_Type=Integer32
_FlashCompactFailure_Object=MibScalar
flashCompactFailure=_FlashCompactFailure_Object((1,3,6,1,4,1,207,8,4,4,4,31,12),_FlashCompactFailure_Type())
flashCompactFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCompactFailure.setStatus(_A)
_FlashVerifyFailure_Type=Integer32
_FlashVerifyFailure_Object=MibScalar
flashVerifyFailure=_FlashVerifyFailure_Object((1,3,6,1,4,1,207,8,4,4,4,31,13),_FlashVerifyFailure_Type())
flashVerifyFailure.setMaxAccess(_C)
if mibBuilder.loadTexts:flashVerifyFailure.setStatus(_A)
flashFailureTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,31,0,1))
flashFailureTrap.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:flashFailureTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'flash':flash,'flashTrap':flashTrap,'flashFailureTrap':flashFailureTrap,_D:flashGetFailure,_E:flashOpenFailure,_F:flashReadFailure,_G:flashCloseFailure,_H:flashCompleteFailure,_I:flashWriteFailure,_J:flashCreateFailure,_K:flashPutFailure,_L:flashDeleteFailure,_M:flashCheckFailure,_N:flashEraseFailure,_O:flashCompactFailure,_P:flashVerifyFailure})