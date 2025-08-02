_P='tnpPort'
_O='tfPort'
_N='npPort'
_M='stPort'
_L='portOperDown'
_K='fvPort'
_J='tePort'
_I='nxPort'
_H='nlPort'
_G='tlPort'
_F='sdPort'
_E='fxPort'
_D='flPort'
_C='unknown'
_B='auto'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoModules,=mibBuilder.importSymbols('CISCO-SMI','ciscoModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
storageTextualConventions=ModuleIdentity((1,3,6,1,4,1,9,12,4))
if mibBuilder.loadTexts:storageTextualConventions.setRevisions(('2024-08-20 00:00','2021-02-12 00:00','2016-11-30 00:00','2012-08-08 00:00','2011-07-26 00:00','2010-12-24 00:00','2008-05-16 00:00','2005-12-17 00:00','2004-05-18 00:00','2003-09-26 00:00','2003-08-07 00:00','2002-10-04 00:00','2002-09-24 00:00'))
class VsanIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class DomainId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,239))
class DomainIdOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,239))
class FcAddressId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
class FcNameId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class FcNameIdOrZero(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8),ValueSizeConstraint(16,16))
class FcClassOfServices(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('classF',0),('class1',1),('class2',2),('class3',3),('class4',4),('class5',5),('class6',6)))
class FcPortTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*((_B,1),('fPort',2),(_D,3),('ePort',4),('bPort',5),(_E,6),(_F,7),(_G,8),('nPort',9),(_H,10),(_I,11),(_J,12),(_K,13),(_L,14),(_M,15),(_N,16),(_O,17),(_P,18)))
class FcPortTxTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_C,1),('longWaveLaser',2),('shortWaveLaser',3),('longWaveLaserCostReduced',4),('electrical',5),('tenGigBaseSr',6),('tenGigBaseLr',7),('tenGigBaseEr',8),('tenGigBaseLx4',9),('tenGigBaseSw',10),('tenGigBaseLw',11),('tenGigBaseEw',12)))
class FcPortModuleTypes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*((_C,1),('other',2),('gbic',3),('embedded',4),('glm',5),('gbicWithSerialID',6),('gbicWithoutSerialID',7),('sfpWithSerialID',8),('sfpWithoutSerialID',9),('xfp',10),('x2Short',11),('x2Medium',12),('x2Tall',13),('xpakShort',14),('xpakMedium',15),('xpakTall',16),('xenpak',17),('sfpDwdm',18),('qsfp',19),('x2Dwdm',20)))
class FcIfSpeed(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_B,1),('oneG',2),('twoG',3),('fourG',4),('autoMaxTwoG',5),('eightG',6),('autoMaxFourG',7),('tenG',8),('autoMaxEightG',9),('sixteenG',10),('autoMaxSixteenG',11),('thirtyTwoG',12),('autoMaxThirtyTwoG',13),('fiftyG',14),('sixtyFourG',15),('autoMaxSixtyFourG',16)))
class PortMemberList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
class FcAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3),ValueSizeConstraint(8,8))
class FcAddressType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('wwn',1),('fcid',2)))
class InterfaceOperMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)));namedValues=NamedValues(*((_B,1),('fPort',2),(_D,3),('ePort',4),('bPort',5),(_E,6),(_F,7),(_G,8),('nPort',9),(_H,10),(_I,11),(_J,12),(_K,13),(_L,14),(_M,15),('mgmtPort',16),('ipsPort',17),('evPort',18),(_N,19),(_O,20),(_P,21)))
class FcIfServiceStateType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inService',1),('outOfService',2)))
class FcIfSfpDiagLevelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_C,1),('normal',2),('lowWarning',3),('lowAlarm',4),('highWarning',5),('highAlarm',6)))
mibBuilder.exportSymbols('CISCO-ST-TC',**{'VsanIndex':VsanIndex,'DomainId':DomainId,'DomainIdOrZero':DomainIdOrZero,'FcAddressId':FcAddressId,'FcNameId':FcNameId,'FcNameIdOrZero':FcNameIdOrZero,'FcClassOfServices':FcClassOfServices,'FcPortTypes':FcPortTypes,'FcPortTxTypes':FcPortTxTypes,'FcPortModuleTypes':FcPortModuleTypes,'FcIfSpeed':FcIfSpeed,'PortMemberList':PortMemberList,'FcAddress':FcAddress,'FcAddressType':FcAddressType,'InterfaceOperMode':InterfaceOperMode,'FcIfServiceStateType':FcIfServiceStateType,'FcIfSfpDiagLevelType':FcIfSfpDiagLevelType,'storageTextualConventions':storageTextualConventions})