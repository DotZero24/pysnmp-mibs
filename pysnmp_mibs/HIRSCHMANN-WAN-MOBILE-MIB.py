_C='Integer32'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmWanMgmt,=mibBuilder.importSymbols('HIRSCHMANN-WAN-MIB','hmWanMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hmWanMobileMib=ModuleIdentity((1,3,6,1,4,1,248,40,1,4))
if mibBuilder.loadTexts:hmWanMobileMib.setRevisions(('2016-08-09 00:00',))
class _HmWanMobileTechnology_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,4,6,8,10,12,14,16,18,20,22,24)));namedValues=NamedValues(*(('none',0),('gprs',2),('edge',4),('umts',6),('hsdpa',8),('hsupa',10),('hspa',12),('lte',14),('cdma',16),('evdo',18),('evdo0',20),('evdoA',22),('evdoB',24)))
_HmWanMobileTechnology_Type.__name__=_C
_HmWanMobileTechnology_Object=MibScalar
hmWanMobileTechnology=_HmWanMobileTechnology_Object((1,3,6,1,4,1,248,40,1,4,1),_HmWanMobileTechnology_Type())
hmWanMobileTechnology.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileTechnology.setStatus(_B)
_HmWanMobilePLMN_Type=OctetString
_HmWanMobilePLMN_Object=MibScalar
hmWanMobilePLMN=_HmWanMobilePLMN_Object((1,3,6,1,4,1,248,40,1,4,2),_HmWanMobilePLMN_Type())
hmWanMobilePLMN.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobilePLMN.setStatus(_B)
_HmWanMobileCell_Type=OctetString
_HmWanMobileCell_Object=MibScalar
hmWanMobileCell=_HmWanMobileCell_Object((1,3,6,1,4,1,248,40,1,4,3),_HmWanMobileCell_Type())
hmWanMobileCell.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileCell.setStatus(_B)
_HmWanMobileChannel_Type=OctetString
_HmWanMobileChannel_Object=MibScalar
hmWanMobileChannel=_HmWanMobileChannel_Object((1,3,6,1,4,1,248,40,1,4,4),_HmWanMobileChannel_Type())
hmWanMobileChannel.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileChannel.setStatus(_B)
_HmWanMobileSignalStrength_Type=Integer32
_HmWanMobileSignalStrength_Object=MibScalar
hmWanMobileSignalStrength=_HmWanMobileSignalStrength_Object((1,3,6,1,4,1,248,40,1,4,5),_HmWanMobileSignalStrength_Type())
hmWanMobileSignalStrength.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileSignalStrength.setStatus(_B)
_HmWanMobileChannelN1_Type=OctetString
_HmWanMobileChannelN1_Object=MibScalar
hmWanMobileChannelN1=_HmWanMobileChannelN1_Object((1,3,6,1,4,1,248,40,1,4,6),_HmWanMobileChannelN1_Type())
hmWanMobileChannelN1.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileChannelN1.setStatus(_B)
_HmWanMobileSignalStrengthN1_Type=Integer32
_HmWanMobileSignalStrengthN1_Object=MibScalar
hmWanMobileSignalStrengthN1=_HmWanMobileSignalStrengthN1_Object((1,3,6,1,4,1,248,40,1,4,7),_HmWanMobileSignalStrengthN1_Type())
hmWanMobileSignalStrengthN1.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileSignalStrengthN1.setStatus(_B)
_HmWanMobileChannelN2_Type=OctetString
_HmWanMobileChannelN2_Object=MibScalar
hmWanMobileChannelN2=_HmWanMobileChannelN2_Object((1,3,6,1,4,1,248,40,1,4,8),_HmWanMobileChannelN2_Type())
hmWanMobileChannelN2.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileChannelN2.setStatus(_B)
_HmWanMobileSignalStrengthN2_Type=Integer32
_HmWanMobileSignalStrengthN2_Object=MibScalar
hmWanMobileSignalStrengthN2=_HmWanMobileSignalStrengthN2_Object((1,3,6,1,4,1,248,40,1,4,9),_HmWanMobileSignalStrengthN2_Type())
hmWanMobileSignalStrengthN2.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileSignalStrengthN2.setStatus(_B)
_HmWanMobileChannelN3_Type=OctetString
_HmWanMobileChannelN3_Object=MibScalar
hmWanMobileChannelN3=_HmWanMobileChannelN3_Object((1,3,6,1,4,1,248,40,1,4,10),_HmWanMobileChannelN3_Type())
hmWanMobileChannelN3.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileChannelN3.setStatus(_B)
_HmWanMobileSignalStrengthN3_Type=Integer32
_HmWanMobileSignalStrengthN3_Object=MibScalar
hmWanMobileSignalStrengthN3=_HmWanMobileSignalStrengthN3_Object((1,3,6,1,4,1,248,40,1,4,11),_HmWanMobileSignalStrengthN3_Type())
hmWanMobileSignalStrengthN3.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileSignalStrengthN3.setStatus(_B)
_HmWanMobileChannelN4_Type=OctetString
_HmWanMobileChannelN4_Object=MibScalar
hmWanMobileChannelN4=_HmWanMobileChannelN4_Object((1,3,6,1,4,1,248,40,1,4,12),_HmWanMobileChannelN4_Type())
hmWanMobileChannelN4.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileChannelN4.setStatus(_B)
_HmWanMobileSignalStrengthN4_Type=Integer32
_HmWanMobileSignalStrengthN4_Object=MibScalar
hmWanMobileSignalStrengthN4=_HmWanMobileSignalStrengthN4_Object((1,3,6,1,4,1,248,40,1,4,13),_HmWanMobileSignalStrengthN4_Type())
hmWanMobileSignalStrengthN4.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileSignalStrengthN4.setStatus(_B)
_HmWanMobileChannelN5_Type=OctetString
_HmWanMobileChannelN5_Object=MibScalar
hmWanMobileChannelN5=_HmWanMobileChannelN5_Object((1,3,6,1,4,1,248,40,1,4,14),_HmWanMobileChannelN5_Type())
hmWanMobileChannelN5.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileChannelN5.setStatus(_B)
_HmWanMobileSignalStrengthN5_Type=Integer32
_HmWanMobileSignalStrengthN5_Object=MibScalar
hmWanMobileSignalStrengthN5=_HmWanMobileSignalStrengthN5_Object((1,3,6,1,4,1,248,40,1,4,15),_HmWanMobileSignalStrengthN5_Type())
hmWanMobileSignalStrengthN5.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileSignalStrengthN5.setStatus(_B)
_HmWanMobileUpTime_Type=TimeTicks
_HmWanMobileUpTime_Object=MibScalar
hmWanMobileUpTime=_HmWanMobileUpTime_Object((1,3,6,1,4,1,248,40,1,4,16),_HmWanMobileUpTime_Type())
hmWanMobileUpTime.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileUpTime.setStatus(_B)
_HmWanMobileConnect_Type=Counter32
_HmWanMobileConnect_Object=MibScalar
hmWanMobileConnect=_HmWanMobileConnect_Object((1,3,6,1,4,1,248,40,1,4,17),_HmWanMobileConnect_Type())
hmWanMobileConnect.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileConnect.setStatus(_B)
_HmWanMobileDisconnect_Type=Counter32
_HmWanMobileDisconnect_Object=MibScalar
hmWanMobileDisconnect=_HmWanMobileDisconnect_Object((1,3,6,1,4,1,248,40,1,4,18),_HmWanMobileDisconnect_Type())
hmWanMobileDisconnect.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileDisconnect.setStatus(_B)
class _HmWanMobileCard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('primary',0),('secondary',1),('tertiary',2)))
_HmWanMobileCard_Type.__name__=_C
_HmWanMobileCard_Object=MibScalar
hmWanMobileCard=_HmWanMobileCard_Object((1,3,6,1,4,1,248,40,1,4,19),_HmWanMobileCard_Type())
hmWanMobileCard.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileCard.setStatus(_B)
_HmWanMobileIPAddress_Type=IpAddress
_HmWanMobileIPAddress_Object=MibScalar
hmWanMobileIPAddress=_HmWanMobileIPAddress_Object((1,3,6,1,4,1,248,40,1,4,20),_HmWanMobileIPAddress_Type())
hmWanMobileIPAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileIPAddress.setStatus(_B)
_HmWanMobileLatency_Type=Integer32
_HmWanMobileLatency_Object=MibScalar
hmWanMobileLatency=_HmWanMobileLatency_Object((1,3,6,1,4,1,248,40,1,4,21),_HmWanMobileLatency_Type())
hmWanMobileLatency.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLatency.setStatus(_B)
_HmWanMobileReportPeriod_Type=Integer32
_HmWanMobileReportPeriod_Object=MibScalar
hmWanMobileReportPeriod=_HmWanMobileReportPeriod_Object((1,3,6,1,4,1,248,40,1,4,22),_HmWanMobileReportPeriod_Type())
hmWanMobileReportPeriod.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileReportPeriod.setStatus(_B)
class _HmWanMobileRegistration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('unknown',0),('idle',1),('search',2),('denied',3),('home',4),('foregien',5)))
_HmWanMobileRegistration_Type.__name__=_C
_HmWanMobileRegistration_Object=MibScalar
hmWanMobileRegistration=_HmWanMobileRegistration_Object((1,3,6,1,4,1,248,40,1,4,23),_HmWanMobileRegistration_Type())
hmWanMobileRegistration.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileRegistration.setStatus(_B)
_HmWanMobileOperator_Type=OctetString
_HmWanMobileOperator_Object=MibScalar
hmWanMobileOperator=_HmWanMobileOperator_Object((1,3,6,1,4,1,248,40,1,4,24),_HmWanMobileOperator_Type())
hmWanMobileOperator.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileOperator.setStatus(_B)
_HmWanMobileLAC_Type=OctetString
_HmWanMobileLAC_Object=MibScalar
hmWanMobileLAC=_HmWanMobileLAC_Object((1,3,6,1,4,1,248,40,1,4,25),_HmWanMobileLAC_Type())
hmWanMobileLAC.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileLAC.setStatus(_B)
_HmWanMobileSignalQuality_Type=Integer32
_HmWanMobileSignalQuality_Object=MibScalar
hmWanMobileSignalQuality=_HmWanMobileSignalQuality_Object((1,3,6,1,4,1,248,40,1,4,26),_HmWanMobileSignalQuality_Type())
hmWanMobileSignalQuality.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileSignalQuality.setStatus(_B)
_HmWanMobileCSQ_Type=Integer32
_HmWanMobileCSQ_Object=MibScalar
hmWanMobileCSQ=_HmWanMobileCSQ_Object((1,3,6,1,4,1,248,40,1,4,27),_HmWanMobileCSQ_Type())
hmWanMobileCSQ.setMaxAccess(_A)
if mibBuilder.loadTexts:hmWanMobileCSQ.setStatus(_B)
mibBuilder.exportSymbols('HIRSCHMANN-WAN-MOBILE-MIB',**{'hmWanMobileMib':hmWanMobileMib,'hmWanMobileTechnology':hmWanMobileTechnology,'hmWanMobilePLMN':hmWanMobilePLMN,'hmWanMobileCell':hmWanMobileCell,'hmWanMobileChannel':hmWanMobileChannel,'hmWanMobileSignalStrength':hmWanMobileSignalStrength,'hmWanMobileChannelN1':hmWanMobileChannelN1,'hmWanMobileSignalStrengthN1':hmWanMobileSignalStrengthN1,'hmWanMobileChannelN2':hmWanMobileChannelN2,'hmWanMobileSignalStrengthN2':hmWanMobileSignalStrengthN2,'hmWanMobileChannelN3':hmWanMobileChannelN3,'hmWanMobileSignalStrengthN3':hmWanMobileSignalStrengthN3,'hmWanMobileChannelN4':hmWanMobileChannelN4,'hmWanMobileSignalStrengthN4':hmWanMobileSignalStrengthN4,'hmWanMobileChannelN5':hmWanMobileChannelN5,'hmWanMobileSignalStrengthN5':hmWanMobileSignalStrengthN5,'hmWanMobileUpTime':hmWanMobileUpTime,'hmWanMobileConnect':hmWanMobileConnect,'hmWanMobileDisconnect':hmWanMobileDisconnect,'hmWanMobileCard':hmWanMobileCard,'hmWanMobileIPAddress':hmWanMobileIPAddress,'hmWanMobileLatency':hmWanMobileLatency,'hmWanMobileReportPeriod':hmWanMobileReportPeriod,'hmWanMobileRegistration':hmWanMobileRegistration,'hmWanMobileOperator':hmWanMobileOperator,'hmWanMobileLAC':hmWanMobileLAC,'hmWanMobileSignalQuality':hmWanMobileSignalQuality,'hmWanMobileCSQ':hmWanMobileCSQ})