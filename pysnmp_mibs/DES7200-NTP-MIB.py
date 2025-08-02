_O='myNtpMIBGroups'
_N='current'
_M='myntpSysRefTime'
_L='myntpSysRefId'
_K='myntpSysRootDispersion'
_J='myntpSysRootDelay'
_I='myntpSysPrecision'
_H='myntpSysStratum'
_G='myntpSysLeap'
_F='read-write'
_E='NotificationType'
_D='Integer32'
_C='read-only'
_B='mandatory'
_A='DES7200-NTP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
myNtpMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,49))
if mibBuilder.loadTexts:myNtpMIB.setRevisions(('2009-05-14 00:00',))
class NTPTimeStamp(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class NTPLeapIndicator(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noWarning',0),('addSecond',1),('subtractSecond',2),('alarm',3)))
class NTPSignedTimeValue(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPUnsignedTimeValue(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class NTPStratum(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
class NTPRefId(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_MyNtpMIBObjects_ObjectIdentity=ObjectIdentity
myNtpMIBObjects=_MyNtpMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,49,1))
_MyntpSystem_ObjectIdentity=ObjectIdentity
myntpSystem=_MyntpSystem_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,49,1,1))
_MyntpSysLeap_Type=NTPLeapIndicator
_MyntpSysLeap_Object=MibScalar
myntpSysLeap=_MyntpSysLeap_Object((1,3,6,1,4,1,171,10,97,2,49,1,1,1),_MyntpSysLeap_Type())
myntpSysLeap.setMaxAccess(_F)
if mibBuilder.loadTexts:myntpSysLeap.setStatus(_B)
_MyntpSysStratum_Type=NTPStratum
_MyntpSysStratum_Object=MibScalar
myntpSysStratum=_MyntpSysStratum_Object((1,3,6,1,4,1,171,10,97,2,49,1,1,2),_MyntpSysStratum_Type())
myntpSysStratum.setMaxAccess(_F)
if mibBuilder.loadTexts:myntpSysStratum.setStatus(_B)
class _MyntpSysPrecision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-24,24))
_MyntpSysPrecision_Type.__name__=_D
_MyntpSysPrecision_Object=MibScalar
myntpSysPrecision=_MyntpSysPrecision_Object((1,3,6,1,4,1,171,10,97,2,49,1,1,3),_MyntpSysPrecision_Type())
myntpSysPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:myntpSysPrecision.setStatus(_B)
_MyntpSysRootDelay_Type=NTPSignedTimeValue
_MyntpSysRootDelay_Object=MibScalar
myntpSysRootDelay=_MyntpSysRootDelay_Object((1,3,6,1,4,1,171,10,97,2,49,1,1,4),_MyntpSysRootDelay_Type())
myntpSysRootDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:myntpSysRootDelay.setStatus(_B)
_MyntpSysRootDispersion_Type=NTPUnsignedTimeValue
_MyntpSysRootDispersion_Object=MibScalar
myntpSysRootDispersion=_MyntpSysRootDispersion_Object((1,3,6,1,4,1,171,10,97,2,49,1,1,5),_MyntpSysRootDispersion_Type())
myntpSysRootDispersion.setMaxAccess(_C)
if mibBuilder.loadTexts:myntpSysRootDispersion.setStatus(_B)
_MyntpSysRefId_Type=NTPRefId
_MyntpSysRefId_Object=MibScalar
myntpSysRefId=_MyntpSysRefId_Object((1,3,6,1,4,1,171,10,97,2,49,1,1,6),_MyntpSysRefId_Type())
myntpSysRefId.setMaxAccess(_C)
if mibBuilder.loadTexts:myntpSysRefId.setStatus(_B)
_MyntpSysRefTime_Type=NTPTimeStamp
_MyntpSysRefTime_Object=MibScalar
myntpSysRefTime=_MyntpSysRefTime_Object((1,3,6,1,4,1,171,10,97,2,49,1,1,7),_MyntpSysRefTime_Type())
myntpSysRefTime.setMaxAccess(_C)
if mibBuilder.loadTexts:myntpSysRefTime.setStatus(_B)
_MyNtpMIBConformance_ObjectIdentity=ObjectIdentity
myNtpMIBConformance=_MyNtpMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,49,2))
_MyNtpMIBCompliances_ObjectIdentity=ObjectIdentity
myNtpMIBCompliances=_MyNtpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,49,2,1))
_MyNtpMIBGroups_ObjectIdentity=ObjectIdentity
myNtpMIBGroups=_MyNtpMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,49,2,2))
myNtpSysGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,49,2,2,1))
myNtpSysGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:myNtpSysGroup.setStatus(_N)
myNtpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,49,2,1,1))
myNtpMIBCompliance.setObjects((_A,_O))
if mibBuilder.loadTexts:myNtpMIBCompliance.setStatus(_N)
mibBuilder.exportSymbols(_A,**{'NTPTimeStamp':NTPTimeStamp,'NTPLeapIndicator':NTPLeapIndicator,'NTPSignedTimeValue':NTPSignedTimeValue,'NTPUnsignedTimeValue':NTPUnsignedTimeValue,'NTPStratum':NTPStratum,'NTPRefId':NTPRefId,'myNtpMIB':myNtpMIB,'myNtpMIBObjects':myNtpMIBObjects,'myntpSystem':myntpSystem,_G:myntpSysLeap,_H:myntpSysStratum,_I:myntpSysPrecision,_J:myntpSysRootDelay,_K:myntpSysRootDispersion,_L:myntpSysRefId,_M:myntpSysRefTime,'myNtpMIBConformance':myNtpMIBConformance,'myNtpMIBCompliances':myNtpMIBCompliances,'myNtpMIBCompliance':myNtpMIBCompliance,_O:myNtpMIBGroups,'myNtpSysGroup':myNtpSysGroup})