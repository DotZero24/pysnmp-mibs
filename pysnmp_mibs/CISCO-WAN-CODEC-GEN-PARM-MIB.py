_H='vismCodecGenParmGroup'
_G='vismCodecJitterInitialDelay'
_F='vismCodecJitterDelayMode'
_E='read-write'
_D='vismCodecIndex'
_C='Integer32'
_B='CISCO-WAN-CODEC-GEN-PARM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoWanCodecGenParmMIB=ModuleIdentity((1,3,6,1,4,1,351,150,21))
if mibBuilder.loadTexts:ciscoWanCodecGenParmMIB.setRevisions(('2004-03-17 00:00','2004-01-30 00:00','2003-05-23 00:00','2001-09-10 00:00','2001-08-21 15:00','2001-08-02 15:00','2001-06-15 15:00','2001-03-20 15:00'))
_CiscoWanCodecGenParmMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWanCodecGenParmMIBObjects=_CiscoWanCodecGenParmMIBObjects_ObjectIdentity((1,3,6,1,4,1,351,150,21,1))
_VismCodecGenParmGrp_ObjectIdentity=ObjectIdentity
vismCodecGenParmGrp=_VismCodecGenParmGrp_ObjectIdentity((1,3,6,1,4,1,351,150,21,1,1))
_VismCodecGenParmTable_Object=MibTable
vismCodecGenParmTable=_VismCodecGenParmTable_Object((1,3,6,1,4,1,351,150,21,1,1,1))
if mibBuilder.loadTexts:vismCodecGenParmTable.setStatus(_A)
_VismCodecGenParmEntry_Object=MibTableRow
vismCodecGenParmEntry=_VismCodecGenParmEntry_Object((1,3,6,1,4,1,351,150,21,1,1,1,1))
vismCodecGenParmEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:vismCodecGenParmEntry.setStatus(_A)
class _VismCodecIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,11,12,13,14,15)));namedValues=NamedValues(*(('g711u',1),('g711a',2),('g726r32000',3),('g729a',4),('g729ab',5),('clearChannel',6),('g726r16000',7),('g726r24000',8),('g726r40000',9),('g723h',11),('g723ah',12),('g723l',13),('g723al',14),('lossless',15)))
_VismCodecIndex_Type.__name__=_C
_VismCodecIndex_Object=MibTableColumn
vismCodecIndex=_VismCodecIndex_Object((1,3,6,1,4,1,351,150,21,1,1,1,1,1),_VismCodecIndex_Type())
vismCodecIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:vismCodecIndex.setStatus(_A)
class _VismCodecJitterDelayMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fixed',1),('adaptive',2),('fixedWithTimeStamp',3)))
_VismCodecJitterDelayMode_Type.__name__=_C
_VismCodecJitterDelayMode_Object=MibTableColumn
vismCodecJitterDelayMode=_VismCodecJitterDelayMode_Object((1,3,6,1,4,1,351,150,21,1,1,1,1,2),_VismCodecJitterDelayMode_Type())
vismCodecJitterDelayMode.setMaxAccess(_E)
if mibBuilder.loadTexts:vismCodecJitterDelayMode.setStatus(_A)
class _VismCodecJitterInitialDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,55,60,65,70,75,80,85,90,95,100)));namedValues=NamedValues(*(('zero',1),('two',2),('three',3),('four',4),('five',5),('six',6),('seven',7),('eight',8),('nine',9),('ten',10),('eleven',11),('twelve',12),('thirteen',13),('fourteen',14),('fifteen',15),('sixteen',16),('seventeen',17),('eighteen',18),('nineteen',19),('twenty',20),('twentyone',21),('twentytwo',22),('twentythree',23),('twentyfour',24),('twentyfive',25),('twentysix',26),('twentyseven',27),('twentyeight',28),('twentynine',29),('thirty',30),('thirtyone',31),('thirtytwo',32),('thirtythree',33),('thirtyfour',34),('thirtyfive',35),('thirtysix',36),('thirtyseven',37),('thirtyeight',38),('thirtynine',39),('fourty',40),('fortyone',41),('fortytwo',42),('fortythree',43),('fortyfour',44),('fortyfive',45),('fortysix',46),('fortyseven',47),('fortyeight',48),('fortynine',49),('fifty',50),('fiftyfive',55),('sixty',60),('sixtyfive',65),('seventy',70),('seventyfive',75),('eighty',80),('eightyfive',85),('ninty',90),('ninetyfive',95),('hundred',100)))
_VismCodecJitterInitialDelay_Type.__name__=_C
_VismCodecJitterInitialDelay_Object=MibTableColumn
vismCodecJitterInitialDelay=_VismCodecJitterInitialDelay_Object((1,3,6,1,4,1,351,150,21,1,1,1,1,3),_VismCodecJitterInitialDelay_Type())
vismCodecJitterInitialDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:vismCodecJitterInitialDelay.setStatus(_A)
_VismCodecGenParmNotificationPrefix_ObjectIdentity=ObjectIdentity
vismCodecGenParmNotificationPrefix=_VismCodecGenParmNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,351,150,21,2))
_VismCodecGenParmNotifications_ObjectIdentity=ObjectIdentity
vismCodecGenParmNotifications=_VismCodecGenParmNotifications_ObjectIdentity((1,3,6,1,4,1,351,150,21,2,0))
_VismCodecGenParmMIBConformance_ObjectIdentity=ObjectIdentity
vismCodecGenParmMIBConformance=_VismCodecGenParmMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,21,3))
_VismCodecGenParmMIBCompliances_ObjectIdentity=ObjectIdentity
vismCodecGenParmMIBCompliances=_VismCodecGenParmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,21,3,1))
_VismCodecGenParmMIBGroups_ObjectIdentity=ObjectIdentity
vismCodecGenParmMIBGroups=_VismCodecGenParmMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,21,3,2))
vismCodecGenParmGroup=ObjectGroup((1,3,6,1,4,1,351,150,21,3,2,1))
vismCodecGenParmGroup.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:vismCodecGenParmGroup.setStatus(_A)
vismCodecGenParmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,21,3,1,1))
vismCodecGenParmMIBCompliance.setObjects((_B,_H))
if mibBuilder.loadTexts:vismCodecGenParmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWanCodecGenParmMIB':ciscoWanCodecGenParmMIB,'ciscoWanCodecGenParmMIBObjects':ciscoWanCodecGenParmMIBObjects,'vismCodecGenParmGrp':vismCodecGenParmGrp,'vismCodecGenParmTable':vismCodecGenParmTable,'vismCodecGenParmEntry':vismCodecGenParmEntry,_D:vismCodecIndex,_F:vismCodecJitterDelayMode,_G:vismCodecJitterInitialDelay,'vismCodecGenParmNotificationPrefix':vismCodecGenParmNotificationPrefix,'vismCodecGenParmNotifications':vismCodecGenParmNotifications,'vismCodecGenParmMIBConformance':vismCodecGenParmMIBConformance,'vismCodecGenParmMIBCompliances':vismCodecGenParmMIBCompliances,'vismCodecGenParmMIBCompliance':vismCodecGenParmMIBCompliance,'vismCodecGenParmMIBGroups':vismCodecGenParmMIBGroups,_H:vismCodecGenParmGroup})