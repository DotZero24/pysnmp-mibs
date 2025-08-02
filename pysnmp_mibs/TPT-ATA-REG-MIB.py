_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_reg,=mibBuilder.importSymbols('TIPPINGPOINT-REG-MIB','tpt-reg')
tpt_ata_family=ModuleIdentity((1,3,6,1,4,1,10734,1,10))
if mibBuilder.loadTexts:tpt_ata_family.setRevisions(('2016-05-25 18:54','2015-07-30 17:35'))
_Tpt_model_ata_network_ObjectIdentity=ObjectIdentity
tpt_model_ata_network=_Tpt_model_ata_network_ObjectIdentity((1,3,6,1,4,1,10734,1,10,1))
if mibBuilder.loadTexts:tpt_model_ata_network.setStatus(_A)
_Tpt_model_ata_mail_ObjectIdentity=ObjectIdentity
tpt_model_ata_mail=_Tpt_model_ata_mail_ObjectIdentity((1,3,6,1,4,1,10734,1,10,2))
if mibBuilder.loadTexts:tpt_model_ata_mail.setStatus(_A)
mibBuilder.exportSymbols('TPT-ATA-REG-MIB',**{'tpt-ata-family':tpt_ata_family,'tpt-model-ata-network':tpt_model_ata_network,'tpt-model-ata-mail':tpt_model_ata_mail})