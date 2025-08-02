_F='statKey3Index'
_E='statKey2Index'
_D='statKey1Index'
_C='HALON-SP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
halonSecuritySP=ModuleIdentity((1,3,6,1,4,1,33234,1,1))
if mibBuilder.loadTexts:halonSecuritySP.setRevisions(('2013-02-07 11:32',))
_HalonSecurity_ObjectIdentity=ObjectIdentity
halonSecurity=_HalonSecurity_ObjectIdentity((1,3,6,1,4,1,33234))
_HalonSecurityProducts_ObjectIdentity=ObjectIdentity
halonSecurityProducts=_HalonSecurityProducts_ObjectIdentity((1,3,6,1,4,1,33234,1))
_HalonSecuritySPObjects_ObjectIdentity=ObjectIdentity
halonSecuritySPObjects=_HalonSecuritySPObjects_ObjectIdentity((1,3,6,1,4,1,33234,1,1,1))
_SerialNumber_Type=OctetString
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,33234,1,1,1,1),_SerialNumber_Type())
serialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_ConfigurationRevision_Type=Integer32
_ConfigurationRevision_Object=MibScalar
configurationRevision=_ConfigurationRevision_Object((1,3,6,1,4,1,33234,1,1,1,2),_ConfigurationRevision_Type())
configurationRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:configurationRevision.setStatus(_A)
_MailQueueLength_Type=Counter64
_MailQueueLength_Object=MibScalar
mailQueueLength=_MailQueueLength_Object((1,3,6,1,4,1,33234,1,1,1,3),_MailQueueLength_Type())
mailQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:mailQueueLength.setStatus(_A)
_QuarantinedMessages_Type=Counter64
_QuarantinedMessages_Object=MibScalar
quarantinedMessages=_QuarantinedMessages_Object((1,3,6,1,4,1,33234,1,1,1,4),_QuarantinedMessages_Type())
quarantinedMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:quarantinedMessages.setStatus(_A)
_StatTable_Object=MibTable
statTable=_StatTable_Object((1,3,6,1,4,1,33234,1,1,1,5))
if mibBuilder.loadTexts:statTable.setStatus(_A)
_StatEntry_Object=MibTableRow
statEntry=_StatEntry_Object((1,3,6,1,4,1,33234,1,1,1,5,1))
statEntry.setIndexNames((0,_C,_D),(0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:statEntry.setStatus(_A)
_StatKey1Index_Type=OctetString
_StatKey1Index_Object=MibTableColumn
statKey1Index=_StatKey1Index_Object((1,3,6,1,4,1,33234,1,1,1,5,1,1),_StatKey1Index_Type())
statKey1Index.setMaxAccess(_B)
if mibBuilder.loadTexts:statKey1Index.setStatus(_A)
_StatKey2Index_Type=OctetString
_StatKey2Index_Object=MibTableColumn
statKey2Index=_StatKey2Index_Object((1,3,6,1,4,1,33234,1,1,1,5,1,2),_StatKey2Index_Type())
statKey2Index.setMaxAccess(_B)
if mibBuilder.loadTexts:statKey2Index.setStatus(_A)
_StatKey3Index_Type=OctetString
_StatKey3Index_Object=MibTableColumn
statKey3Index=_StatKey3Index_Object((1,3,6,1,4,1,33234,1,1,1,5,1,3),_StatKey3Index_Type())
statKey3Index.setMaxAccess(_B)
if mibBuilder.loadTexts:statKey3Index.setStatus(_A)
_StatCount_Type=Counter64
_StatCount_Object=MibTableColumn
statCount=_StatCount_Object((1,3,6,1,4,1,33234,1,1,1,5,1,4),_StatCount_Type())
statCount.setMaxAccess(_B)
if mibBuilder.loadTexts:statCount.setStatus(_A)
_StatCreated_Type=Integer32
_StatCreated_Object=MibTableColumn
statCreated=_StatCreated_Object((1,3,6,1,4,1,33234,1,1,1,5,1,5),_StatCreated_Type())
statCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:statCreated.setStatus(_A)
_StatUpdated_Type=Integer32
_StatUpdated_Object=MibTableColumn
statUpdated=_StatUpdated_Object((1,3,6,1,4,1,33234,1,1,1,5,1,6),_StatUpdated_Type())
statUpdated.setMaxAccess(_B)
if mibBuilder.loadTexts:statUpdated.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'halonSecurity':halonSecurity,'halonSecurityProducts':halonSecurityProducts,'halonSecuritySP':halonSecuritySP,'halonSecuritySPObjects':halonSecuritySPObjects,'serialNumber':serialNumber,'configurationRevision':configurationRevision,'mailQueueLength':mailQueueLength,'quarantinedMessages':quarantinedMessages,'statTable':statTable,'statEntry':statEntry,_D:statKey1Index,_E:statKey2Index,_F:statKey3Index,'statCount':statCount,'statCreated':statCreated,'statUpdated':statUpdated})