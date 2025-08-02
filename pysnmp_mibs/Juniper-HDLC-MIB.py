_V='juniHdlcGroup4'
_U='juniHdlcGroup3'
_T='juniHdlcGroup2'
_S='juniHdlcGroup'
_R='juniHdlcIfIdleCharacter'
_Q='octets'
_P='juniHdlcIfIndex'
_O='juniHdlcIfForceDteAck'
_N='juniHdlcIfClockRate'
_M='juniHdlcIfClockMode'
_L='juniHdlcIfDataPolarity'
_K='juniHdlcIfCrcSize'
_J='juniHdlcIfMru'
_I='juniHdlcIfMtu'
_H='juniHdlcIfLowerIfIndex'
_G='juniHdlcIfRowStatus'
_F='juniHdlcNextIfIndex'
_E='obsolete'
_D='Integer32'
_C='read-create'
_B='current'
_A='Juniper-HDLC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniNextIfIndex,=mibBuilder.importSymbols('Juniper-TC','JuniNextIfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
juniHdlcMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,9))
if mibBuilder.loadTexts:juniHdlcMIB.setRevisions(('2003-10-03 19:25','2002-09-16 21:44','2001-11-28 13:43','2001-03-22 14:30','2000-01-26 00:00','1999-07-28 00:00','1998-11-13 00:00'))
_JuniHdlcObjects_ObjectIdentity=ObjectIdentity
juniHdlcObjects=_JuniHdlcObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,9,1))
_JuniHdlcNextIfIndex_Type=JuniNextIfIndex
_JuniHdlcNextIfIndex_Object=MibScalar
juniHdlcNextIfIndex=_JuniHdlcNextIfIndex_Object((1,3,6,1,4,1,4874,2,2,9,1,1),_JuniHdlcNextIfIndex_Type())
juniHdlcNextIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:juniHdlcNextIfIndex.setStatus(_B)
_JuniHdlcIfTable_Object=MibTable
juniHdlcIfTable=_JuniHdlcIfTable_Object((1,3,6,1,4,1,4874,2,2,9,1,2))
if mibBuilder.loadTexts:juniHdlcIfTable.setStatus(_B)
_JuniHdlcIfEntry_Object=MibTableRow
juniHdlcIfEntry=_JuniHdlcIfEntry_Object((1,3,6,1,4,1,4874,2,2,9,1,2,1))
juniHdlcIfEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:juniHdlcIfEntry.setStatus(_B)
_JuniHdlcIfIndex_Type=InterfaceIndex
_JuniHdlcIfIndex_Object=MibTableColumn
juniHdlcIfIndex=_JuniHdlcIfIndex_Object((1,3,6,1,4,1,4874,2,2,9,1,2,1,1),_JuniHdlcIfIndex_Type())
juniHdlcIfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:juniHdlcIfIndex.setStatus(_B)
_JuniHdlcIfRowStatus_Type=RowStatus
_JuniHdlcIfRowStatus_Object=MibTableColumn
juniHdlcIfRowStatus=_JuniHdlcIfRowStatus_Object((1,3,6,1,4,1,4874,2,2,9,1,2,1,2),_JuniHdlcIfRowStatus_Type())
juniHdlcIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHdlcIfRowStatus.setStatus(_B)
_JuniHdlcIfLowerIfIndex_Type=InterfaceIndexOrZero
_JuniHdlcIfLowerIfIndex_Object=MibTableColumn
juniHdlcIfLowerIfIndex=_JuniHdlcIfLowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,9,1,2,1,3),_JuniHdlcIfLowerIfIndex_Type())
juniHdlcIfLowerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHdlcIfLowerIfIndex.setStatus(_B)
class _JuniHdlcIfMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32763))
_JuniHdlcIfMtu_Type.__name__=_D
_JuniHdlcIfMtu_Object=MibTableColumn
juniHdlcIfMtu=_JuniHdlcIfMtu_Object((1,3,6,1,4,1,4874,2,2,9,1,2,1,4),_JuniHdlcIfMtu_Type())
juniHdlcIfMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHdlcIfMtu.setStatus(_B)
if mibBuilder.loadTexts:juniHdlcIfMtu.setUnits(_Q)
class _JuniHdlcIfMru_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32763))
_JuniHdlcIfMru_Type.__name__=_D
_JuniHdlcIfMru_Object=MibTableColumn
juniHdlcIfMru=_JuniHdlcIfMru_Object((1,3,6,1,4,1,4874,2,2,9,1,2,1,5),_JuniHdlcIfMru_Type())
juniHdlcIfMru.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHdlcIfMru.setStatus(_B)
if mibBuilder.loadTexts:juniHdlcIfMru.setUnits(_Q)
class _JuniHdlcIfCrcSize_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('crc16',1),('crc32',2)))
_JuniHdlcIfCrcSize_Type.__name__=_D
_JuniHdlcIfCrcSize_Object=MibTableColumn
juniHdlcIfCrcSize=_JuniHdlcIfCrcSize_Object((1,3,6,1,4,1,4874,2,2,9,1,2,1,6),_JuniHdlcIfCrcSize_Type())
juniHdlcIfCrcSize.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHdlcIfCrcSize.setStatus(_B)
class _JuniHdlcIfDataPolarity_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('inverted',1)))
_JuniHdlcIfDataPolarity_Type.__name__=_D
_JuniHdlcIfDataPolarity_Object=MibTableColumn
juniHdlcIfDataPolarity=_JuniHdlcIfDataPolarity_Object((1,3,6,1,4,1,4874,2,2,9,1,2,1,7),_JuniHdlcIfDataPolarity_Type())
juniHdlcIfDataPolarity.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHdlcIfDataPolarity.setStatus(_B)
class _JuniHdlcIfClockMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('hdlcClockUnsupported',0),('hdlcClockInternal',1),('hdlcClockLine',2)))
_JuniHdlcIfClockMode_Type.__name__=_D
_JuniHdlcIfClockMode_Object=MibTableColumn
juniHdlcIfClockMode=_JuniHdlcIfClockMode_Object((1,3,6,1,4,1,4874,2,2,9,1,2,1,8),_JuniHdlcIfClockMode_Type())
juniHdlcIfClockMode.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHdlcIfClockMode.setStatus(_B)
class _JuniHdlcIfClockRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('hdlcClockRateUnsupported',0),('hdlcClockRate34At368Mhz',1),('hdlcClockRate44At736Mhz',2)))
_JuniHdlcIfClockRate_Type.__name__=_D
_JuniHdlcIfClockRate_Object=MibTableColumn
juniHdlcIfClockRate=_JuniHdlcIfClockRate_Object((1,3,6,1,4,1,4874,2,2,9,1,2,1,9),_JuniHdlcIfClockRate_Type())
juniHdlcIfClockRate.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHdlcIfClockRate.setStatus(_B)
class _JuniHdlcIfForceDteAck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceDteAckUnsupported',0),('forceDteAckNormal',1),('forceDteAckForced',2)))
_JuniHdlcIfForceDteAck_Type.__name__=_D
_JuniHdlcIfForceDteAck_Object=MibTableColumn
juniHdlcIfForceDteAck=_JuniHdlcIfForceDteAck_Object((1,3,6,1,4,1,4874,2,2,9,1,2,1,10),_JuniHdlcIfForceDteAck_Type())
juniHdlcIfForceDteAck.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHdlcIfForceDteAck.setStatus(_B)
class _JuniHdlcIfIdleCharacter_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('idleCharacterFlags',0),('idleCharacterMarks',1)))
_JuniHdlcIfIdleCharacter_Type.__name__=_D
_JuniHdlcIfIdleCharacter_Object=MibTableColumn
juniHdlcIfIdleCharacter=_JuniHdlcIfIdleCharacter_Object((1,3,6,1,4,1,4874,2,2,9,1,2,1,11),_JuniHdlcIfIdleCharacter_Type())
juniHdlcIfIdleCharacter.setMaxAccess(_C)
if mibBuilder.loadTexts:juniHdlcIfIdleCharacter.setStatus(_B)
_JuniHdlcConformance_ObjectIdentity=ObjectIdentity
juniHdlcConformance=_JuniHdlcConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,9,4))
_JuniHdlcCompliances_ObjectIdentity=ObjectIdentity
juniHdlcCompliances=_JuniHdlcCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,9,4,1))
_JuniHdlcGroups_ObjectIdentity=ObjectIdentity
juniHdlcGroups=_JuniHdlcGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,9,4,2))
juniHdlcGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,9,4,2,1))
juniHdlcGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:juniHdlcGroup.setStatus(_E)
juniHdlcGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,9,4,2,2))
juniHdlcGroup2.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:juniHdlcGroup2.setStatus(_E)
juniHdlcGroup3=ObjectGroup((1,3,6,1,4,1,4874,2,2,9,4,2,3))
juniHdlcGroup3.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:juniHdlcGroup3.setStatus(_E)
juniHdlcGroup4=ObjectGroup((1,3,6,1,4,1,4874,2,2,9,4,2,4))
juniHdlcGroup4.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_R)))
if mibBuilder.loadTexts:juniHdlcGroup4.setStatus(_B)
juniHdlcCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,9,4,1,1))
juniHdlcCompliance.setObjects((_A,_S))
if mibBuilder.loadTexts:juniHdlcCompliance.setStatus(_E)
juniHdlcCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,9,4,1,2))
juniHdlcCompliance2.setObjects((_A,_T))
if mibBuilder.loadTexts:juniHdlcCompliance2.setStatus(_E)
juniHdlcCompliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,9,4,1,3))
juniHdlcCompliance3.setObjects((_A,_U))
if mibBuilder.loadTexts:juniHdlcCompliance3.setStatus(_E)
juniHdlcCompliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,9,4,1,4))
juniHdlcCompliance4.setObjects((_A,_V))
if mibBuilder.loadTexts:juniHdlcCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniHdlcMIB':juniHdlcMIB,'juniHdlcObjects':juniHdlcObjects,_F:juniHdlcNextIfIndex,'juniHdlcIfTable':juniHdlcIfTable,'juniHdlcIfEntry':juniHdlcIfEntry,_P:juniHdlcIfIndex,_G:juniHdlcIfRowStatus,_H:juniHdlcIfLowerIfIndex,_I:juniHdlcIfMtu,_J:juniHdlcIfMru,_K:juniHdlcIfCrcSize,_L:juniHdlcIfDataPolarity,_M:juniHdlcIfClockMode,_N:juniHdlcIfClockRate,_O:juniHdlcIfForceDteAck,_R:juniHdlcIfIdleCharacter,'juniHdlcConformance':juniHdlcConformance,'juniHdlcCompliances':juniHdlcCompliances,'juniHdlcCompliance':juniHdlcCompliance,'juniHdlcCompliance2':juniHdlcCompliance2,'juniHdlcCompliance3':juniHdlcCompliance3,'juniHdlcCompliance4':juniHdlcCompliance4,'juniHdlcGroups':juniHdlcGroups,_S:juniHdlcGroup,_T:juniHdlcGroup2,_U:juniHdlcGroup3,_V:juniHdlcGroup4})