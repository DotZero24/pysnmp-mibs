_P='lowerLayerDown'
_O='notPresent'
_N='read-write'
_M='InterfaceIndex'
_L='DisplayString'
_K='dormant'
_J='unknown'
_I='ctDs0ifIndex'
_H='CT-DS0ent-MIB'
_G='deprecated'
_F='testing'
_E='down'
_D='up'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cabletron,=mibBuilder.importSymbols('CTRON-OIDS','cabletron')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','TextualConvention')
class InterfaceIndex(Integer32):0
class IANActDs0ifType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54)));namedValues=NamedValues(*(('other',1),('regular1822',2),('hdh1822',3),('ddnX25',4),('rfc877x25',5),('ethernetCsmacd',6),('iso88023Csmacd',7),('iso88024TokenBus',8),('iso88025TokenRing',9),('iso88026Man',10),('starLan',11),('proteon10Mbit',12),('proteon80Mbit',13),('hyperchannel',14),('fddi',15),('lapb',16),('sdlc',17),('ds1',18),('e1',19),('basicISDN',20),('primaryISDN',21),('propPointToPointSerial',22),('ppp',23),('softwareLoopback',24),('eon',25),('ethernet3Mbit',26),('nsip',27),('slip',28),('ultra',29),('ds3',30),('sip',31),('frameRelay',32),('rs232',33),('para',34),('arcnet',35),('arcnetPlus',36),('atm',37),('miox25',38),('sonet',39),('x25ple',40),('iso88022llc',41),('localTalk',42),('smdsDxi',43),('frameRelayService',44),('v35',45),('hssi',46),('hippi',47),('modem',48),('aal5',49),('sonetPath',50),('sonetVT',51),('smdsIcip',52),('propVirtual',53),('propMultiplexor',54)))
_CtSSA_ObjectIdentity=ObjectIdentity
ctSSA=_CtSSA_ObjectIdentity((1,3,6,1,4,1,52,4497))
_CtDs0Mib_ObjectIdentity=ObjectIdentity
ctDs0Mib=_CtDs0Mib_ObjectIdentity((1,3,6,1,4,1,52,4497,20))
_CtDs0ifNumber_Type=Integer32
_CtDs0ifNumber_Object=MibScalar
ctDs0ifNumber=_CtDs0ifNumber_Object((1,3,6,1,4,1,52,4497,20,1),_CtDs0ifNumber_Type())
ctDs0ifNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifNumber.setStatus(_A)
_CtDs0ifTable_Object=MibTable
ctDs0ifTable=_CtDs0ifTable_Object((1,3,6,1,4,1,52,4497,20,2))
if mibBuilder.loadTexts:ctDs0ifTable.setStatus(_A)
_CtDs0ifEntry_Object=MibTableRow
ctDs0ifEntry=_CtDs0ifEntry_Object((1,3,6,1,4,1,52,4497,20,2,1))
ctDs0ifEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:ctDs0ifEntry.setStatus(_A)
class _CtDs0ifIndex_Type(InterfaceIndex):subtypeSpec=InterfaceIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CtDs0ifIndex_Type.__name__=_M
_CtDs0ifIndex_Object=MibTableColumn
ctDs0ifIndex=_CtDs0ifIndex_Object((1,3,6,1,4,1,52,4497,20,2,1,1),_CtDs0ifIndex_Type())
ctDs0ifIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifIndex.setStatus(_A)
class _CtDs0ifDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtDs0ifDescr_Type.__name__=_L
_CtDs0ifDescr_Object=MibTableColumn
ctDs0ifDescr=_CtDs0ifDescr_Object((1,3,6,1,4,1,52,4497,20,2,1,2),_CtDs0ifDescr_Type())
ctDs0ifDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifDescr.setStatus(_A)
_CtDs0ifType_Type=IANActDs0ifType
_CtDs0ifType_Object=MibTableColumn
ctDs0ifType=_CtDs0ifType_Object((1,3,6,1,4,1,52,4497,20,2,1,3),_CtDs0ifType_Type())
ctDs0ifType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifType.setStatus(_A)
_CtDs0ifMtu_Type=Integer32
_CtDs0ifMtu_Object=MibTableColumn
ctDs0ifMtu=_CtDs0ifMtu_Object((1,3,6,1,4,1,52,4497,20,2,1,4),_CtDs0ifMtu_Type())
ctDs0ifMtu.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifMtu.setStatus(_A)
_CtDs0ifSpeed_Type=Gauge32
_CtDs0ifSpeed_Object=MibTableColumn
ctDs0ifSpeed=_CtDs0ifSpeed_Object((1,3,6,1,4,1,52,4497,20,2,1,5),_CtDs0ifSpeed_Type())
ctDs0ifSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifSpeed.setStatus(_A)
_CtDs0ifPhysAddress_Type=PhysAddress
_CtDs0ifPhysAddress_Object=MibTableColumn
ctDs0ifPhysAddress=_CtDs0ifPhysAddress_Object((1,3,6,1,4,1,52,4497,20,2,1,6),_CtDs0ifPhysAddress_Type())
ctDs0ifPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifPhysAddress.setStatus(_A)
class _CtDs0ifAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_CtDs0ifAdminStatus_Type.__name__=_C
_CtDs0ifAdminStatus_Object=MibTableColumn
ctDs0ifAdminStatus=_CtDs0ifAdminStatus_Object((1,3,6,1,4,1,52,4497,20,2,1,7),_CtDs0ifAdminStatus_Type())
ctDs0ifAdminStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:ctDs0ifAdminStatus.setStatus(_A)
class _CtDs0ifOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3),(_J,4),(_K,5)))
_CtDs0ifOperStatus_Type.__name__=_C
_CtDs0ifOperStatus_Object=MibTableColumn
ctDs0ifOperStatus=_CtDs0ifOperStatus_Object((1,3,6,1,4,1,52,4497,20,2,1,8),_CtDs0ifOperStatus_Type())
ctDs0ifOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifOperStatus.setStatus(_A)
_CtDs0ifLastChange_Type=TimeTicks
_CtDs0ifLastChange_Object=MibTableColumn
ctDs0ifLastChange=_CtDs0ifLastChange_Object((1,3,6,1,4,1,52,4497,20,2,1,9),_CtDs0ifLastChange_Type())
ctDs0ifLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifLastChange.setStatus(_A)
_CtDs0ifInOctets_Type=Counter32
_CtDs0ifInOctets_Object=MibTableColumn
ctDs0ifInOctets=_CtDs0ifInOctets_Object((1,3,6,1,4,1,52,4497,20,2,1,10),_CtDs0ifInOctets_Type())
ctDs0ifInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifInOctets.setStatus(_A)
_CtDs0ifInUcastPkts_Type=Counter32
_CtDs0ifInUcastPkts_Object=MibTableColumn
ctDs0ifInUcastPkts=_CtDs0ifInUcastPkts_Object((1,3,6,1,4,1,52,4497,20,2,1,11),_CtDs0ifInUcastPkts_Type())
ctDs0ifInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifInUcastPkts.setStatus(_A)
_CtDs0ifInNUcastPkts_Type=Counter32
_CtDs0ifInNUcastPkts_Object=MibTableColumn
ctDs0ifInNUcastPkts=_CtDs0ifInNUcastPkts_Object((1,3,6,1,4,1,52,4497,20,2,1,12),_CtDs0ifInNUcastPkts_Type())
ctDs0ifInNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifInNUcastPkts.setStatus(_G)
_CtDs0ifInDiscards_Type=Counter32
_CtDs0ifInDiscards_Object=MibTableColumn
ctDs0ifInDiscards=_CtDs0ifInDiscards_Object((1,3,6,1,4,1,52,4497,20,2,1,13),_CtDs0ifInDiscards_Type())
ctDs0ifInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifInDiscards.setStatus(_A)
_CtDs0ifInErrors_Type=Counter32
_CtDs0ifInErrors_Object=MibTableColumn
ctDs0ifInErrors=_CtDs0ifInErrors_Object((1,3,6,1,4,1,52,4497,20,2,1,14),_CtDs0ifInErrors_Type())
ctDs0ifInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifInErrors.setStatus(_A)
_CtDs0ifInUnknownProtos_Type=Counter32
_CtDs0ifInUnknownProtos_Object=MibTableColumn
ctDs0ifInUnknownProtos=_CtDs0ifInUnknownProtos_Object((1,3,6,1,4,1,52,4497,20,2,1,15),_CtDs0ifInUnknownProtos_Type())
ctDs0ifInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifInUnknownProtos.setStatus(_A)
_CtDs0ifOutOctets_Type=Counter32
_CtDs0ifOutOctets_Object=MibTableColumn
ctDs0ifOutOctets=_CtDs0ifOutOctets_Object((1,3,6,1,4,1,52,4497,20,2,1,16),_CtDs0ifOutOctets_Type())
ctDs0ifOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifOutOctets.setStatus(_A)
_CtDs0ifOutUcastPkts_Type=Counter32
_CtDs0ifOutUcastPkts_Object=MibTableColumn
ctDs0ifOutUcastPkts=_CtDs0ifOutUcastPkts_Object((1,3,6,1,4,1,52,4497,20,2,1,17),_CtDs0ifOutUcastPkts_Type())
ctDs0ifOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifOutUcastPkts.setStatus(_A)
_CtDs0ifOutNUcastPkts_Type=Counter32
_CtDs0ifOutNUcastPkts_Object=MibTableColumn
ctDs0ifOutNUcastPkts=_CtDs0ifOutNUcastPkts_Object((1,3,6,1,4,1,52,4497,20,2,1,18),_CtDs0ifOutNUcastPkts_Type())
ctDs0ifOutNUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifOutNUcastPkts.setStatus(_G)
_CtDs0ifOutDiscards_Type=Counter32
_CtDs0ifOutDiscards_Object=MibTableColumn
ctDs0ifOutDiscards=_CtDs0ifOutDiscards_Object((1,3,6,1,4,1,52,4497,20,2,1,19),_CtDs0ifOutDiscards_Type())
ctDs0ifOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifOutDiscards.setStatus(_A)
_CtDs0ifOutErrors_Type=Counter32
_CtDs0ifOutErrors_Object=MibTableColumn
ctDs0ifOutErrors=_CtDs0ifOutErrors_Object((1,3,6,1,4,1,52,4497,20,2,1,20),_CtDs0ifOutErrors_Type())
ctDs0ifOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifOutErrors.setStatus(_A)
_CtDs0ifOutQLen_Type=Gauge32
_CtDs0ifOutQLen_Object=MibTableColumn
ctDs0ifOutQLen=_CtDs0ifOutQLen_Object((1,3,6,1,4,1,52,4497,20,2,1,21),_CtDs0ifOutQLen_Type())
ctDs0ifOutQLen.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifOutQLen.setStatus(_G)
_CtDs0ifSpecific_Type=ObjectIdentifier
_CtDs0ifSpecific_Object=MibTableColumn
ctDs0ifSpecific=_CtDs0ifSpecific_Object((1,3,6,1,4,1,52,4497,20,2,1,22),_CtDs0ifSpecific_Type())
ctDs0ifSpecific.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDs0ifSpecific.setStatus(_G)
_CtDsx0Mib_ObjectIdentity=ObjectIdentity
ctDsx0Mib=_CtDsx0Mib_ObjectIdentity((1,3,6,1,4,1,52,4497,21))
_CtDsx0ConfigTable_Object=MibTable
ctDsx0ConfigTable=_CtDsx0ConfigTable_Object((1,3,6,1,4,1,52,4497,21,1))
if mibBuilder.loadTexts:ctDsx0ConfigTable.setStatus(_A)
_CtDsx0ConfigEntry_Object=MibTableRow
ctDsx0ConfigEntry=_CtDsx0ConfigEntry_Object((1,3,6,1,4,1,52,4497,21,1,1))
ctDsx0ConfigEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:ctDsx0ConfigEntry.setStatus(_A)
_CtDsx0ConfigLineId_Type=DisplayString
_CtDsx0ConfigLineId_Object=MibTableColumn
ctDsx0ConfigLineId=_CtDsx0ConfigLineId_Object((1,3,6,1,4,1,52,4497,21,1,1,1),_CtDsx0ConfigLineId_Type())
ctDsx0ConfigLineId.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDsx0ConfigLineId.setStatus(_A)
class _CtDsx0ConfigAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3),(_J,4),(_K,5),(_O,6),(_P,7)))
_CtDsx0ConfigAdminStatus_Type.__name__=_C
_CtDsx0ConfigAdminStatus_Object=MibTableColumn
ctDsx0ConfigAdminStatus=_CtDsx0ConfigAdminStatus_Object((1,3,6,1,4,1,52,4497,21,1,1,2),_CtDsx0ConfigAdminStatus_Type())
ctDsx0ConfigAdminStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:ctDsx0ConfigAdminStatus.setStatus(_A)
class _CtDsx0ConfigOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3),(_J,4),(_K,5),(_O,6),(_P,7)))
_CtDsx0ConfigOperStatus_Type.__name__=_C
_CtDsx0ConfigOperStatus_Object=MibTableColumn
ctDsx0ConfigOperStatus=_CtDsx0ConfigOperStatus_Object((1,3,6,1,4,1,52,4497,21,1,1,3),_CtDsx0ConfigOperStatus_Type())
ctDsx0ConfigOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDsx0ConfigOperStatus.setStatus(_A)
mibBuilder.exportSymbols(_H,**{_M:InterfaceIndex,'IANActDs0ifType':IANActDs0ifType,'ctSSA':ctSSA,'ctDs0Mib':ctDs0Mib,'ctDs0ifNumber':ctDs0ifNumber,'ctDs0ifTable':ctDs0ifTable,'ctDs0ifEntry':ctDs0ifEntry,_I:ctDs0ifIndex,'ctDs0ifDescr':ctDs0ifDescr,'ctDs0ifType':ctDs0ifType,'ctDs0ifMtu':ctDs0ifMtu,'ctDs0ifSpeed':ctDs0ifSpeed,'ctDs0ifPhysAddress':ctDs0ifPhysAddress,'ctDs0ifAdminStatus':ctDs0ifAdminStatus,'ctDs0ifOperStatus':ctDs0ifOperStatus,'ctDs0ifLastChange':ctDs0ifLastChange,'ctDs0ifInOctets':ctDs0ifInOctets,'ctDs0ifInUcastPkts':ctDs0ifInUcastPkts,'ctDs0ifInNUcastPkts':ctDs0ifInNUcastPkts,'ctDs0ifInDiscards':ctDs0ifInDiscards,'ctDs0ifInErrors':ctDs0ifInErrors,'ctDs0ifInUnknownProtos':ctDs0ifInUnknownProtos,'ctDs0ifOutOctets':ctDs0ifOutOctets,'ctDs0ifOutUcastPkts':ctDs0ifOutUcastPkts,'ctDs0ifOutNUcastPkts':ctDs0ifOutNUcastPkts,'ctDs0ifOutDiscards':ctDs0ifOutDiscards,'ctDs0ifOutErrors':ctDs0ifOutErrors,'ctDs0ifOutQLen':ctDs0ifOutQLen,'ctDs0ifSpecific':ctDs0ifSpecific,'ctDsx0Mib':ctDsx0Mib,'ctDsx0ConfigTable':ctDsx0ConfigTable,'ctDsx0ConfigEntry':ctDsx0ConfigEntry,'ctDsx0ConfigLineId':ctDsx0ConfigLineId,'ctDsx0ConfigAdminStatus':ctDsx0ConfigAdminStatus,'ctDsx0ConfigOperStatus':ctDsx0ConfigOperStatus})